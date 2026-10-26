# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T16:07:28.904479+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0446` n `13`; crypto_alt avg `-0.2214` n `237`; crypto_major avg `-0.1466` n `8`; equity avg `-0.0647` n `154`; fx avg `0.0062` n `6`; index avg `-0.0016` n `27`; metal avg `-0.0045` n `20`; unknown avg `-0.1222` n `1230`
- 1h: commodity avg `0.3466` n `13`; crypto_alt avg `-0.4974` n `237`; crypto_major avg `-0.278` n `8`; equity avg `-0.0892` n `154`; fx avg `0.005` n `6`; index avg `-0.0499` n `27`; metal avg `-0.0661` n `20`; unknown avg `0.198` n `1226`
- 4h: commodity avg `0.3795` n `13`; crypto_alt avg `0.5411` n `237`; crypto_major avg `0.2984` n `8`; equity avg `0.8393` n `153`; fx avg `0.0238` n `6`; index avg `0.124` n `27`; metal avg `-0.0025` n `20`; unknown avg `599.6734` n `1154`
- 24h: commodity avg `0.0702` n `13`; crypto_alt avg `0.2083` n `237`; crypto_major avg `0.1882` n `8`; equity avg `0.7509` n `153`; fx avg `0.0727` n `6`; index avg `-0.0529` n `27`; metal avg `0.1496` n `20`; unknown avg `790.1186` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2315`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
