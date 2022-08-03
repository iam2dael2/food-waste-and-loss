-- Total Produksi Sampah Masing-Masing Negara
select 
	nama_alias negara,
	`rumah tangga` + restoran + retail total_sampah 
from flw f 
group by 1
order by 2 desc 