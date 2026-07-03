# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T07:22:30.672302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.017` n `12`; crypto_alt avg `-0.1082` n `229`; crypto_major avg `-0.0145` n `8`; equity avg `-0.0381` n `88`; fx avg `-0.0174` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0701` n `20`; unknown avg `0.0832` n `765`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.1077` n `229`; crypto_major avg `-0.0458` n `8`; equity avg `-0.0677` n `88`; fx avg `-0.0765` n `6`; index avg `0.0039` n `25`; metal avg `0.054` n `20`; unknown avg `-0.0985` n `763`
- 4h: commodity avg `0.0574` n `12`; crypto_alt avg `0.1895` n `229`; crypto_major avg `0.4324` n `8`; equity avg `0.5036` n `88`; fx avg `-0.1842` n `6`; index avg `0.1945` n `25`; metal avg `-0.0484` n `20`; unknown avg `-0.1698` n `743`
- 24h: commodity avg `0.5165` n `12`; crypto_alt avg `2.508` n `228`; crypto_major avg `3.8024` n `8`; equity avg `0.8148` n `88`; fx avg `-0.1766` n `6`; index avg `0.3047` n `25`; metal avg `1.3047` n `20`; unknown avg `5.7272` n `741`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
