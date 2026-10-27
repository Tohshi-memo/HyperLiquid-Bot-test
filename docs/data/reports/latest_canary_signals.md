# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T19:37:28.524392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0584` n `13`; crypto_alt avg `0.0158` n `238`; crypto_major avg `0.0954` n `8`; equity avg `0.0629` n `154`; fx avg `0.0016` n `6`; index avg `0.0209` n `27`; metal avg `0.0226` n `20`; unknown avg `0.0583` n `1238`
- 1h: commodity avg `0.1443` n `13`; crypto_alt avg `-0.0241` n `238`; crypto_major avg `0.0683` n `8`; equity avg `0.2207` n `154`; fx avg `0.0031` n `6`; index avg `0.0541` n `27`; metal avg `0.0865` n `20`; unknown avg `74.5378` n `1234`
- 4h: commodity avg `0.0103` n `13`; crypto_alt avg `0.4325` n `238`; crypto_major avg `0.481` n `8`; equity avg `0.5099` n `154`; fx avg `-0.0018` n `6`; index avg `0.0644` n `27`; metal avg `0.039` n `20`; unknown avg `1.5315` n `1226`
- 24h: commodity avg `-0.4583` n `13`; crypto_alt avg `1.103` n `237`; crypto_major avg `1.2631` n `8`; equity avg `1.7248` n `154`; fx avg `-0.0504` n `6`; index avg `0.4357` n `27`; metal avg `0.2215` n `20`; unknown avg `27.2063` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.23`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
