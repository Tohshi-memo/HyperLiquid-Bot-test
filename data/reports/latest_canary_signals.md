# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T20:22:32.669808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.0229` n `230`; crypto_major avg `-0.0432` n `8`; equity avg `-0.0223` n `112`; fx avg `0.008` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0069` n `20`; unknown avg `0.0859` n `785`
- 1h: commodity avg `-0.0162` n `12`; crypto_alt avg `0.1343` n `230`; crypto_major avg `-0.0396` n `8`; equity avg `0.021` n `112`; fx avg `0.0082` n `6`; index avg `-0.0106` n `25`; metal avg `0.0157` n `20`; unknown avg `0.0075` n `785`
- 4h: commodity avg `0.0821` n `12`; crypto_alt avg `0.3796` n `230`; crypto_major avg `-0.1472` n `8`; equity avg `0.1132` n `112`; fx avg `0.01` n `6`; index avg `0.0197` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.3023` n `785`
- 24h: commodity avg `0.096` n `12`; crypto_alt avg `1.4105` n `230`; crypto_major avg `0.0727` n `8`; equity avg `0.2372` n `112`; fx avg `0.0145` n `6`; index avg `0.0309` n `25`; metal avg `0.0994` n `20`; unknown avg `-0.2261` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
