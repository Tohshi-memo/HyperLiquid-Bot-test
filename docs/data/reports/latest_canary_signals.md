# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T16:07:47.016512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0282` n `13`; crypto_alt avg `-0.0929` n `238`; crypto_major avg `-0.0512` n `8`; equity avg `0.1501` n `154`; fx avg `-0.0014` n `6`; index avg `0.0114` n `27`; metal avg `-0.0299` n `20`; unknown avg `2.109` n `1226`
- 1h: commodity avg `0.044` n `13`; crypto_alt avg `0.4912` n `238`; crypto_major avg `0.4309` n `8`; equity avg `0.6285` n `154`; fx avg `-0.004` n `6`; index avg `0.0976` n `27`; metal avg `0.0032` n `20`; unknown avg `6.1451` n `1194`
- 4h: commodity avg `-0.2312` n `13`; crypto_alt avg `1.399` n `238`; crypto_major avg `1.2308` n `8`; equity avg `1.7324` n `154`; fx avg `-0.0348` n `6`; index avg `0.2342` n `27`; metal avg `0.3989` n `20`; unknown avg `1.1937` n `1152`
- 24h: commodity avg `-0.6996` n `13`; crypto_alt avg `0.1086` n `237`; crypto_major avg `0.6393` n `8`; equity avg `1.6003` n `154`; fx avg `-0.0798` n `6`; index avg `0.4149` n `27`; metal avg `0.0919` n `20`; unknown avg `29.3958` n `1042`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2306`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2035`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2012`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
