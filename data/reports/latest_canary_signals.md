# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T18:07:28.157280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0713` n `13`; crypto_alt avg `-0.2074` n `236`; crypto_major avg `-0.0535` n `8`; equity avg `-0.1807` n `151`; fx avg `-0.0079` n `6`; index avg `-0.0397` n `26`; metal avg `-0.0004` n `20`; unknown avg `205.5989` n `1175`
- 1h: commodity avg `0.0688` n `13`; crypto_alt avg `-0.1102` n `236`; crypto_major avg `0.0543` n `8`; equity avg `-0.1749` n `151`; fx avg `-0.0035` n `6`; index avg `-0.0592` n `26`; metal avg `0.0216` n `20`; unknown avg `43.7081` n `1175`
- 4h: commodity avg `0.6631` n `13`; crypto_alt avg `-1.844` n `236`; crypto_major avg `-1.3167` n `8`; equity avg `-1.6339` n `151`; fx avg `-0.0405` n `6`; index avg `-0.3336` n `26`; metal avg `-0.1901` n `20`; unknown avg `1.053` n `1042`
- 24h: commodity avg `0.1364` n `13`; crypto_alt avg `-1.8409` n `236`; crypto_major avg `-1.6075` n `8`; equity avg `-2.3055` n `151`; fx avg `-0.0149` n `6`; index avg `-0.459` n `26`; metal avg `-0.0275` n `20`; unknown avg `-0.3282` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1475`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0989`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0802`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0736`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
