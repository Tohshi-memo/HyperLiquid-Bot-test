# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T09:37:27.868895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.1169` n `231`; crypto_major avg `0.094` n `8`; equity avg `-0.0067` n `127`; fx avg `-0.0059` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.0313` n `791`
- 1h: commodity avg `0.0079` n `12`; crypto_alt avg `0.0785` n `231`; crypto_major avg `0.1493` n `8`; equity avg `-0.003` n `127`; fx avg `-0.0162` n `6`; index avg `-0.0096` n `26`; metal avg `0.0089` n `20`; unknown avg `-0.4373` n `791`
- 4h: commodity avg `0.0212` n `12`; crypto_alt avg `-0.6766` n `231`; crypto_major avg `-0.3736` n `8`; equity avg `0.0185` n `127`; fx avg `-0.0061` n `6`; index avg `-0.012` n `26`; metal avg `0.0092` n `20`; unknown avg `0.0427` n `761`
- 24h: commodity avg `-0.0761` n `12`; crypto_alt avg `-1.9228` n `231`; crypto_major avg `-1.9968` n `8`; equity avg `-1.3361` n `127`; fx avg `-0.0293` n `6`; index avg `-0.136` n `26`; metal avg `-0.6551` n `20`; unknown avg `-0.3739` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
