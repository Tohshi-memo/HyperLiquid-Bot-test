# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T21:07:44.099914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `0.0259` n `230`; crypto_major avg `0.0237` n `8`; equity avg `-0.0348` n `120`; fx avg `-0.0005` n `6`; index avg `0.0111` n `25`; metal avg `0.0253` n `20`; unknown avg `-0.0671` n `789`
- 1h: commodity avg `0.0559` n `12`; crypto_alt avg `-0.134` n `230`; crypto_major avg `-0.0696` n `8`; equity avg `-0.1039` n `120`; fx avg `0.0034` n `6`; index avg `0.0012` n `25`; metal avg `-0.0223` n `20`; unknown avg `0.2808` n `789`
- 4h: commodity avg `0.0987` n `12`; crypto_alt avg `-0.3921` n `230`; crypto_major avg `-0.0057` n `8`; equity avg `-0.5737` n `120`; fx avg `0.0077` n `6`; index avg `-0.0742` n `25`; metal avg `-0.1711` n `20`; unknown avg `-0.0457` n `789`
- 24h: commodity avg `0.3067` n `12`; crypto_alt avg `-0.8082` n `230`; crypto_major avg `0.14` n `8`; equity avg `-4.4293` n `120`; fx avg `-0.0442` n `6`; index avg `-0.6883` n `25`; metal avg `-0.7672` n `20`; unknown avg `-0.2846` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
