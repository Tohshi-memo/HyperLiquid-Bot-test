# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T08:22:29.671038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `13`; crypto_alt avg `0.0249` n `236`; crypto_major avg `0.0105` n `8`; equity avg `0.0111` n `151`; fx avg `0.0064` n `6`; index avg `-0.0136` n `26`; metal avg `0.0028` n `20`; unknown avg `0.0486` n `1193`
- 1h: commodity avg `0.0156` n `13`; crypto_alt avg `-0.0133` n `236`; crypto_major avg `0.0367` n `8`; equity avg `0.0187` n `151`; fx avg `0.0049` n `6`; index avg `0.0073` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.099` n `1175`
- 4h: commodity avg `-0.2394` n `13`; crypto_alt avg `-0.2889` n `236`; crypto_major avg `0.2298` n `8`; equity avg `0.0873` n `151`; fx avg `0.0059` n `6`; index avg `0.0309` n `26`; metal avg `-0.0142` n `20`; unknown avg `0.1787` n `1157`
- 24h: commodity avg `0.3291` n `13`; crypto_alt avg `-1.8371` n `236`; crypto_major avg `-1.1408` n `8`; equity avg `-3.8172` n `151`; fx avg `0.0507` n `6`; index avg `-0.5889` n `26`; metal avg `-0.2486` n `20`; unknown avg `10.3169` n `952`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1815`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1457`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1261`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0743`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
