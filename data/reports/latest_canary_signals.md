# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T06:22:25.821243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `13`; crypto_alt avg `0.0233` n `236`; crypto_major avg `0.0627` n `8`; equity avg `0.0376` n `151`; fx avg `0.0056` n `6`; index avg `-0.0001` n `26`; metal avg `0.0133` n `20`; unknown avg `-0.0136` n `1193`
- 1h: commodity avg `-0.0535` n `13`; crypto_alt avg `-0.0912` n `236`; crypto_major avg `0.0052` n `8`; equity avg `0.0238` n `151`; fx avg `0.0061` n `6`; index avg `0.0133` n `26`; metal avg `0.0061` n `20`; unknown avg `0.3064` n `1175`
- 4h: commodity avg `-0.0496` n `13`; crypto_alt avg `0.1266` n `236`; crypto_major avg `0.2503` n `8`; equity avg `0.1247` n `151`; fx avg `0.0039` n `6`; index avg `0.0449` n `26`; metal avg `0.0279` n `20`; unknown avg `0.779` n `1169`
- 24h: commodity avg `0.611` n `13`; crypto_alt avg `-1.4762` n `236`; crypto_major avg `-1.1185` n `8`; equity avg `-3.6929` n `151`; fx avg `0.0462` n `6`; index avg `-0.5474` n `26`; metal avg `-0.1605` n `20`; unknown avg `40.6271` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1801`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1176`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0973`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0753`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
