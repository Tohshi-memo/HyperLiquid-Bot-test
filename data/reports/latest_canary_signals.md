# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T10:22:28.255009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `0.0167` n `230`; crypto_major avg `0.0319` n `8`; equity avg `-0.0072` n `120`; fx avg `-0.0138` n `6`; index avg `0.0194` n `25`; metal avg `0.0476` n `20`; unknown avg `-0.0821` n `791`
- 1h: commodity avg `-0.0348` n `12`; crypto_alt avg `-0.1411` n `230`; crypto_major avg `-0.114` n `8`; equity avg `-0.5422` n `120`; fx avg `-0.0571` n `6`; index avg `-0.0559` n `25`; metal avg `0.0819` n `20`; unknown avg `-0.0746` n `791`
- 4h: commodity avg `0.0593` n `12`; crypto_alt avg `0.0247` n `230`; crypto_major avg `0.1735` n `8`; equity avg `0.6239` n `120`; fx avg `-0.087` n `6`; index avg `0.1605` n `25`; metal avg `0.1154` n `20`; unknown avg `-0.0648` n `789`
- 24h: commodity avg `0.3803` n `12`; crypto_alt avg `0.1602` n `230`; crypto_major avg `0.3367` n `8`; equity avg `-1.7787` n `120`; fx avg `-0.2049` n `6`; index avg `-0.2009` n `25`; metal avg `-0.4007` n `20`; unknown avg `-0.3133` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
