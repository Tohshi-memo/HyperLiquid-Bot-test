# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T07:20:19.714917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.1004` n `230`; crypto_major avg `-0.0905` n `8`; equity avg `-0.0276` n `102`; fx avg `-0.003` n `6`; index avg `0.0045` n `25`; metal avg `0.0049` n `20`; unknown avg `0.0057` n `781`
- 1h: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.1191` n `230`; crypto_major avg `-0.113` n `8`; equity avg `-0.1008` n `102`; fx avg `-0.0036` n `6`; index avg `-0.0056` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.035` n `781`
- 4h: commodity avg `-0.1063` n `12`; crypto_alt avg `-0.0418` n `230`; crypto_major avg `-0.1152` n `8`; equity avg `-0.0279` n `102`; fx avg `-0.0112` n `6`; index avg `-0.0139` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.0697` n `765`
- 24h: commodity avg `0.8008` n `12`; crypto_alt avg `0.4082` n `230`; crypto_major avg `-1.2744` n `8`; equity avg `-2.1947` n `102`; fx avg `-0.0527` n `6`; index avg `-0.2808` n `25`; metal avg `-0.1577` n `20`; unknown avg `4.8613` n `763`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
