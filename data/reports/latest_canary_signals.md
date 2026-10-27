# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T13:07:30.278953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0235` n `13`; crypto_alt avg `-0.3805` n `238`; crypto_major avg `-0.334` n `8`; equity avg `-0.1475` n `154`; fx avg `-0.0032` n `6`; index avg `-0.0381` n `27`; metal avg `0.0134` n `20`; unknown avg `1.4854` n `1232`
- 1h: commodity avg `-0.0246` n `13`; crypto_alt avg `0.6346` n `238`; crypto_major avg `0.5763` n `8`; equity avg `0.2545` n `154`; fx avg `0.0068` n `6`; index avg `0.0244` n `27`; metal avg `0.1158` n `20`; unknown avg `1.619` n `1232`
- 4h: commodity avg `-0.2151` n `13`; crypto_alt avg `0.2502` n `238`; crypto_major avg `0.57` n `8`; equity avg `0.8547` n `154`; fx avg `0.0344` n `6`; index avg `0.1193` n `27`; metal avg `0.171` n `20`; unknown avg `15.2802` n `1182`
- 24h: commodity avg `-0.1884` n `13`; crypto_alt avg `-0.0784` n `237`; crypto_major avg `0.4338` n `8`; equity avg `1.1826` n `153`; fx avg `-0.0103` n `6`; index avg `0.378` n `27`; metal avg `-0.1231` n `20`; unknown avg `1011.1163` n `1046`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
