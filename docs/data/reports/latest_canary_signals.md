# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T06:07:32.928675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `0.2696` n `237`; crypto_major avg `0.0991` n `8`; equity avg `0.0672` n `151`; fx avg `-0.0003` n `6`; index avg `0.011` n `26`; metal avg `0.0006` n `20`; unknown avg `0.0916` n `1175`
- 1h: commodity avg `0.0161` n `13`; crypto_alt avg `-0.2363` n `237`; crypto_major avg `-0.18` n `8`; equity avg `-0.0806` n `151`; fx avg `0.0021` n `6`; index avg `-0.0095` n `26`; metal avg `-0.006` n `20`; unknown avg `0.0176` n `1175`
- 4h: commodity avg `-0.0345` n `13`; crypto_alt avg `-0.4483` n `237`; crypto_major avg `-0.0444` n `8`; equity avg `0.1715` n `151`; fx avg `-0.0157` n `6`; index avg `0.0417` n `26`; metal avg `0.0079` n `20`; unknown avg `0.0993` n `1169`
- 24h: commodity avg `-0.1135` n `13`; crypto_alt avg `-2.8705` n `236`; crypto_major avg `-0.8221` n `8`; equity avg `-0.8902` n `151`; fx avg `-0.0418` n `6`; index avg `-0.1138` n `26`; metal avg `-0.0531` n `20`; unknown avg `3.8751` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1681`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1328`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1046`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0798`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
