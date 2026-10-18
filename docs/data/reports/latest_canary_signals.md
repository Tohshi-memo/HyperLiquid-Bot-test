# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T12:22:27.388849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `-0.0299` n `237`; crypto_major avg `-0.1089` n `8`; equity avg `0.0399` n `151`; fx avg `0.0039` n `6`; index avg `0.0057` n `26`; metal avg `0.0079` n `20`; unknown avg `0.0107` n `1193`
- 1h: commodity avg `0.0636` n `13`; crypto_alt avg `0.0082` n `237`; crypto_major avg `-0.0276` n `8`; equity avg `0.0638` n `151`; fx avg `0.0034` n `6`; index avg `0.0122` n `26`; metal avg `0.0074` n `20`; unknown avg `0.2254` n `1185`
- 4h: commodity avg `0.0534` n `13`; crypto_alt avg `0.2623` n `237`; crypto_major avg `0.4268` n `8`; equity avg `0.1679` n `151`; fx avg `0.0086` n `6`; index avg `0.031` n `26`; metal avg `0.0263` n `20`; unknown avg `5.3912` n `1089`
- 24h: commodity avg `0.0735` n `13`; crypto_alt avg `-1.899` n `236`; crypto_major avg `-0.0118` n `8`; equity avg `-0.4771` n `151`; fx avg `-0.0565` n `6`; index avg `-0.0397` n `26`; metal avg `-0.0344` n `20`; unknown avg `1.7817` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2064`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1362`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1332`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0748`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
