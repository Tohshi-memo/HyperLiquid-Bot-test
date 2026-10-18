# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T08:37:33.897365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `13`; crypto_alt avg `-0.2376` n `237`; crypto_major avg `-0.1479` n `8`; equity avg `-0.0398` n `151`; fx avg `-0.0007` n `6`; index avg `0.0012` n `26`; metal avg `-0.0006` n `20`; unknown avg `-0.0074` n `1193`
- 1h: commodity avg `0.001` n `13`; crypto_alt avg `-0.156` n `237`; crypto_major avg `-0.0737` n `8`; equity avg `0.0614` n `151`; fx avg `0.0006` n `6`; index avg `0.0123` n `26`; metal avg `-0.001` n `20`; unknown avg `-0.0213` n `1175`
- 4h: commodity avg `-0.0241` n `13`; crypto_alt avg `-0.7202` n `237`; crypto_major avg `-0.4059` n `8`; equity avg `0.1538` n `151`; fx avg `0.0033` n `6`; index avg `0.0338` n `26`; metal avg `-0.012` n `20`; unknown avg `0.1033` n `1157`
- 24h: commodity avg `0.0385` n `13`; crypto_alt avg `-2.7837` n `236`; crypto_major avg `-1.0289` n `8`; equity avg `-0.7376` n `151`; fx avg `-0.0306` n `6`; index avg `-0.0928` n `26`; metal avg `-0.0674` n `20`; unknown avg `4.4208` n `1055`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1756`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1327`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.111`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0825`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
