# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T16:07:30.873351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `13`; crypto_alt avg `-0.0861` n `235`; crypto_major avg `-0.0395` n `8`; equity avg `-0.0804` n `144`; fx avg `-0.0112` n `6`; index avg `-0.0142` n `26`; metal avg `-0.041` n `20`; unknown avg `0.2358` n `1071`
- 1h: commodity avg `-0.1785` n `13`; crypto_alt avg `-0.3194` n `235`; crypto_major avg `-0.3223` n `8`; equity avg `0.0019` n `144`; fx avg `-0.0263` n `6`; index avg `0.005` n `26`; metal avg `-0.0477` n `20`; unknown avg `-0.0169` n `1071`
- 4h: commodity avg `-0.0395` n `13`; crypto_alt avg `-1.2426` n `235`; crypto_major avg `-0.8316` n `8`; equity avg `0.1628` n `144`; fx avg `-0.0559` n `6`; index avg `0.0893` n `26`; metal avg `-0.1604` n `20`; unknown avg `0.7087` n `989`
- 24h: commodity avg `-0.2287` n `13`; crypto_alt avg `-0.054` n `235`; crypto_major avg `0.1626` n `8`; equity avg `0.2473` n `144`; fx avg `-0.1073` n `6`; index avg `0.0739` n `26`; metal avg `0.1483` n `20`; unknown avg `-0.2082` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2028`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
