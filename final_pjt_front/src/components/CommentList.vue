<template>
    <div>
        <CommentListItem
            @delete-comment="deleteComment"
            v-for="(comment, index) in comments"
            :key="index"
            :comment="comment"
        />

    </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem'

export default {
    name: 'CommentList',
    components:{
        CommentListItem,
    },
    props:{
        movie:Object,
        comments:Array,
    },
    computed:{
        nowComments(){
            return this.comments
        }
    },
    methods: {
        deleteComment(id) {
            const nowComments = this.nowComments;
            const index = nowComments.findIndex((obj) => obj.id == id);
            nowComments.splice(index, 1);
        },
    },
    
}
</script>