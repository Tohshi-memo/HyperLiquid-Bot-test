# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T01:52:26.657611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `13`; crypto_alt avg `0.0268` n `235`; crypto_major avg `0.0797` n `8`; equity avg `0.004` n `143`; fx avg `-0.0004` n `6`; index avg `0.0012` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.3365` n `1079`
- 1h: commodity avg `0.056` n `13`; crypto_alt avg `-0.0969` n `235`; crypto_major avg `0.0422` n `8`; equity avg `-0.0041` n `143`; fx avg `-0.0026` n `6`; index avg `-0.0061` n `26`; metal avg `0.0026` n `20`; unknown avg `0.3822` n `1077`
- 4h: commodity avg `-0.0463` n `13`; crypto_alt avg `0.0419` n `235`; crypto_major avg `0.1022` n `8`; equity avg `0.0235` n `143`; fx avg `-0.0015` n `6`; index avg `-0.0092` n `26`; metal avg `0.0001` n `20`; unknown avg `0.1735` n `1069`
- 24h: commodity avg `0.1458` n `13`; crypto_alt avg `1.4535` n `235`; crypto_major avg `0.4655` n `8`; equity avg `0.141` n `143`; fx avg `-0.0331` n `6`; index avg `0.0126` n `26`; metal avg `0.0054` n `20`; unknown avg `0.0182` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2003`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
