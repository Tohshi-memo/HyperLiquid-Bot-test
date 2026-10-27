# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T16:52:30.952008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `13`; crypto_alt avg `-0.1972` n `238`; crypto_major avg `-0.124` n `8`; equity avg `-0.1879` n `154`; fx avg `0.006` n `6`; index avg `-0.0327` n `27`; metal avg `-0.0235` n `20`; unknown avg `1.2504` n `1238`
- 1h: commodity avg `-0.0784` n `13`; crypto_alt avg `-0.1269` n `238`; crypto_major avg `0.062` n `8`; equity avg `0.0411` n `154`; fx avg `0.0019` n `6`; index avg `-0.0158` n `27`; metal avg `-0.0467` n `20`; unknown avg `2.4393` n `1228`
- 4h: commodity avg `-0.233` n `13`; crypto_alt avg `0.3392` n `238`; crypto_major avg `0.4275` n `8`; equity avg `1.2095` n `154`; fx avg `-0.0415` n `6`; index avg `0.1436` n `27`; metal avg `0.2784` n `20`; unknown avg `1.6098` n `1150`
- 24h: commodity avg `-0.7414` n `13`; crypto_alt avg `0.6734` n `237`; crypto_major avg `1.1925` n `8`; equity avg `1.6459` n `154`; fx avg `-0.0718` n `6`; index avg `0.4288` n `27`; metal avg `0.1118` n `20`; unknown avg `29.0549` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2272`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2025`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2013`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
