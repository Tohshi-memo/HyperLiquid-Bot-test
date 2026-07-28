# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T12:22:33.887457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `0.0462` n `230`; crypto_major avg `-0.0448` n `8`; equity avg `-0.0053` n `102`; fx avg `0.0024` n `6`; index avg `0.0113` n `25`; metal avg `0.0394` n `20`; unknown avg `-0.0087` n `774`
- 1h: commodity avg `0.0839` n `12`; crypto_alt avg `-0.0301` n `230`; crypto_major avg `-0.0704` n `8`; equity avg `0.0885` n `102`; fx avg `0.0121` n `6`; index avg `0.075` n `25`; metal avg `0.0687` n `20`; unknown avg `-0.0106` n `774`
- 4h: commodity avg `0.152` n `12`; crypto_alt avg `0.0227` n `230`; crypto_major avg `-0.2626` n `8`; equity avg `-0.5521` n `102`; fx avg `-0.0279` n `6`; index avg `0.0039` n `25`; metal avg `-0.1427` n `20`; unknown avg `-0.1179` n `774`
- 24h: commodity avg `-0.6336` n `12`; crypto_alt avg `-3.4173` n `230`; crypto_major avg `-3.568` n `8`; equity avg `-4.1731` n `102`; fx avg `-0.155` n `6`; index avg `-0.7885` n `25`; metal avg `-0.4742` n `20`; unknown avg `1225.3052` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
