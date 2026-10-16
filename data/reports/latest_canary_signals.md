# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T20:22:27.477762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `13`; crypto_alt avg `-0.2133` n `236`; crypto_major avg `-0.0598` n `8`; equity avg `-0.0305` n `151`; fx avg `-0.003` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0046` n `20`; unknown avg `0.9762` n `1143`
- 1h: commodity avg `-0.0501` n `13`; crypto_alt avg `0.0295` n `236`; crypto_major avg `0.0678` n `8`; equity avg `-0.1809` n `151`; fx avg `0.0064` n `6`; index avg `-0.0332` n `26`; metal avg `0.0146` n `20`; unknown avg `-0.1315` n `1115`
- 4h: commodity avg `0.2789` n `13`; crypto_alt avg `-1.0935` n `236`; crypto_major avg `-0.5341` n `8`; equity avg `-1.2945` n `151`; fx avg `0.0091` n `6`; index avg `-0.2843` n `26`; metal avg `-0.0752` n `20`; unknown avg `-0.2744` n `1112`
- 24h: commodity avg `0.3117` n `13`; crypto_alt avg `-2.0986` n `236`; crypto_major avg `-1.8878` n `8`; equity avg `-3.9745` n `151`; fx avg `0.0179` n `6`; index avg `-0.6671` n `26`; metal avg `-0.1168` n `20`; unknown avg `0.2712` n `896`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1607`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1078`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0809`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0746`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0718`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
