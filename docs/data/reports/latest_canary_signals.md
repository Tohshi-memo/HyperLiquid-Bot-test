# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T06:37:29.873043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `13`; crypto_alt avg `0.0759` n `237`; crypto_major avg `0.0961` n `8`; equity avg `-0.0281` n `151`; fx avg `-0.0035` n `6`; index avg `0.0039` n `26`; metal avg `-0.0319` n `20`; unknown avg `0.0172` n `1194`
- 1h: commodity avg `-0.0265` n `13`; crypto_alt avg `0.1869` n `237`; crypto_major avg `0.1638` n `8`; equity avg `0.35` n `151`; fx avg `-0.0054` n `6`; index avg `0.0502` n `26`; metal avg `-0.0372` n `20`; unknown avg `1.0576` n `1172`
- 4h: commodity avg `-0.073` n `13`; crypto_alt avg `0.089` n `237`; crypto_major avg `0.4159` n `8`; equity avg `0.5127` n `151`; fx avg `0.0155` n `6`; index avg `0.1056` n `26`; metal avg `0.0166` n `20`; unknown avg `5.1742` n `1164`
- 24h: commodity avg `-0.4492` n `13`; crypto_alt avg `0.17` n `237`; crypto_major avg `1.0817` n `8`; equity avg `2.9288` n `151`; fx avg `-0.04` n `6`; index avg `0.5559` n `26`; metal avg `0.278` n `20`; unknown avg `3.354` n `901`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1953`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1411`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1199`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0674`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0661`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0632`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
