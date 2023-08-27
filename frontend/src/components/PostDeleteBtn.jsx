function PostDeleteBtn({ postId }) {
  const handleOnClick = async () => {
    const response = await fetch(`http://127.0.0.1:5000/api/posts/${postId}`, {
      method: "DELETE",
    });

    if (response.ok) {
      window.location.href = "/profile";
    }
  };

  return (
    <button
      onClick={handleOnClick}
      className="bg-red-500 text-slate-200 font-semibold py-3 w-full shadow-lg text-base rounded-lg"
      type="button"
    >
      Delete
    </button>
  );
}

export default PostDeleteBtn;
