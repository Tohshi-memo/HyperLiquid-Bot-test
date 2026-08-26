# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T18:37:36.671635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `-0.0597` n `231`; crypto_major avg `-0.0571` n `8`; equity avg `0.0355` n `122`; fx avg `-0.0048` n `6`; index avg `0.0047` n `25`; metal avg `-0.0087` n `20`; unknown avg `-0.055` n `797`
- 1h: commodity avg `-0.1762` n `12`; crypto_alt avg `-0.0846` n `231`; crypto_major avg `-0.2337` n `8`; equity avg `0.0086` n `122`; fx avg `-0.006` n `6`; index avg `-0.0079` n `25`; metal avg `0.0082` n `20`; unknown avg `-0.0203` n `797`
- 4h: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.223` n `231`; crypto_major avg `0.1301` n `8`; equity avg `0.1983` n `122`; fx avg `-0.0084` n `6`; index avg `0.0172` n `25`; metal avg `-0.1436` n `20`; unknown avg `0.0596` n `797`
- 24h: commodity avg `0.1233` n `12`; crypto_alt avg `-1.9582` n `231`; crypto_major avg `-1.8416` n `8`; equity avg `-0.1864` n `122`; fx avg `-0.0578` n `6`; index avg `0.0242` n `25`; metal avg `-0.3108` n `20`; unknown avg `0.4966` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
