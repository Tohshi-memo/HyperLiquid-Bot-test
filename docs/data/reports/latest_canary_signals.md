# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T14:37:31.323189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `13`; crypto_alt avg `0.0147` n `237`; crypto_major avg `0.0443` n `8`; equity avg `0.0277` n `152`; fx avg `-0.004` n `6`; index avg `-0.0016` n `26`; metal avg `0.0027` n `20`; unknown avg `2.9368` n `1231`
- 1h: commodity avg `0.0376` n `13`; crypto_alt avg `-0.1963` n `237`; crypto_major avg `-0.043` n `8`; equity avg `-0.028` n `152`; fx avg `0.0066` n `6`; index avg `0.0023` n `26`; metal avg `0.0332` n `20`; unknown avg `23.0788` n `1231`
- 4h: commodity avg `-0.0707` n `13`; crypto_alt avg `0.1959` n `237`; crypto_major avg `0.2229` n `8`; equity avg `0.2667` n `152`; fx avg `0.0231` n `6`; index avg `0.0495` n `26`; metal avg `0.0746` n `20`; unknown avg `4.0909` n `1223`
- 24h: commodity avg `-0.1774` n `13`; crypto_alt avg `-0.6971` n `237`; crypto_major avg `0.3027` n `8`; equity avg `0.3624` n `152`; fx avg `0.0188` n `6`; index avg `0.1009` n `26`; metal avg `0.0822` n `20`; unknown avg `22.7271` n `1080`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2223`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
