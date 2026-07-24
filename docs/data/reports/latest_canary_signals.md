# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T11:07:30.259885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0498` n `12`; crypto_alt avg `0.0419` n `230`; crypto_major avg `0.0251` n `8`; equity avg `0.0824` n `100`; fx avg `-0.0108` n `6`; index avg `0.0313` n `25`; metal avg `0.0237` n `20`; unknown avg `0.0082` n `773`
- 1h: commodity avg `0.0677` n `12`; crypto_alt avg `-0.2398` n `230`; crypto_major avg `-0.1652` n `8`; equity avg `-0.1233` n `100`; fx avg `-0.0056` n `6`; index avg `0.0025` n `25`; metal avg `0.0014` n `20`; unknown avg `-0.1252` n `773`
- 4h: commodity avg `-0.1293` n `12`; crypto_alt avg `-0.5152` n `230`; crypto_major avg `-0.4305` n `8`; equity avg `0.3851` n `100`; fx avg `-0.0733` n `6`; index avg `0.0993` n `25`; metal avg `0.2046` n `20`; unknown avg `0.0818` n `772`
- 24h: commodity avg `-0.2407` n `12`; crypto_alt avg `-1.2435` n `230`; crypto_major avg `-1.7143` n `8`; equity avg `-1.6249` n `99`; fx avg `-0.1409` n `6`; index avg `-0.427` n `25`; metal avg `-0.2743` n `20`; unknown avg `0.2026` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1008`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0904`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0838`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
