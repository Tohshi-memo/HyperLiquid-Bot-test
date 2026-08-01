# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T16:07:29.317716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `0.054` n `230`; crypto_major avg `-0.0129` n `8`; equity avg `-0.0041` n `102`; fx avg `0.01` n `6`; index avg `0.0013` n `25`; metal avg `-0.0079` n `20`; unknown avg `-0.0141` n `782`
- 1h: commodity avg `0.0273` n `12`; crypto_alt avg `-0.0766` n `230`; crypto_major avg `-0.1613` n `8`; equity avg `-0.0551` n `102`; fx avg `-0.0075` n `6`; index avg `0.0219` n `25`; metal avg `0.0068` n `20`; unknown avg `0.0095` n `782`
- 4h: commodity avg `-0.0079` n `12`; crypto_alt avg `-0.0902` n `230`; crypto_major avg `0.0146` n `8`; equity avg `-0.1883` n `102`; fx avg `0.0057` n `6`; index avg `0.0251` n `25`; metal avg `0.0152` n `20`; unknown avg `-0.1744` n `782`
- 24h: commodity avg `0.6343` n `12`; crypto_alt avg `0.3153` n `230`; crypto_major avg `-0.4091` n `8`; equity avg `-0.149` n `102`; fx avg `-0.0805` n `6`; index avg `0.055` n `25`; metal avg `0.0641` n `20`; unknown avg `4.1468` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
