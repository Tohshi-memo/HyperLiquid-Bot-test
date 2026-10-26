# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T02:52:28.457606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `6.74` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.1663` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0024` n `13`; crypto_alt avg `-0.2351` n `237`; crypto_major avg `-0.2776` n `8`; equity avg `-0.0972` n `152`; fx avg `0.0083` n `6`; index avg `-0.0202` n `26`; metal avg `0.031` n `20`; unknown avg `1.4041` n `1236`
- 1h: commodity avg `-0.0538` n `13`; crypto_alt avg `-0.3881` n `237`; crypto_major avg `-0.4776` n `8`; equity avg `-0.3547` n `152`; fx avg `-0.0306` n `6`; index avg `-0.0729` n `26`; metal avg `0.0365` n `20`; unknown avg `0.1953` n `1234`
- 4h: commodity avg `-0.1508` n `13`; crypto_alt avg `-1.4528` n `237`; crypto_major avg `-1.3827` n `8`; equity avg `-1.5026` n `152`; fx avg `-0.0061` n `6`; index avg `-0.2164` n `26`; metal avg `-0.1843` n `20`; unknown avg `2.6013` n `1154`
- 24h: commodity avg `-0.61` n `13`; crypto_alt avg `-1.8621` n `237`; crypto_major avg `-1.8065` n `8`; equity avg `-0.9787` n `152`; fx avg `0.0444` n `6`; index avg `-0.0531` n `26`; metal avg `0.0803` n `20`; unknown avg `0.6467` n `989`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
