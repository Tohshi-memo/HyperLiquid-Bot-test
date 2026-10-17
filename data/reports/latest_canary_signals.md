# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T01:52:31.382702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `13`; crypto_alt avg `0.0206` n `236`; crypto_major avg `0.0199` n `8`; equity avg `0.0139` n `151`; fx avg `0.0166` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0065` n `20`; unknown avg `0.0635` n `1191`
- 1h: commodity avg `0.0202` n `13`; crypto_alt avg `-0.1689` n `236`; crypto_major avg `-0.0016` n `8`; equity avg `0.1134` n `151`; fx avg `0.0212` n `6`; index avg `0.0077` n `26`; metal avg `-0.0018` n `20`; unknown avg `3.3075` n `1189`
- 4h: commodity avg `0.088` n `13`; crypto_alt avg `-0.0435` n `236`; crypto_major avg `-0.1865` n `8`; equity avg `0.0666` n `151`; fx avg `0.0133` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0196` n `20`; unknown avg `1.5725` n `1181`
- 24h: commodity avg `0.5609` n `13`; crypto_alt avg `-1.3863` n `236`; crypto_major avg `-1.116` n `8`; equity avg `-3.7563` n `151`; fx avg `-0.0211` n `6`; index avg `-0.619` n `26`; metal avg `-0.031` n `20`; unknown avg `41.5622` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1702`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1146`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0933`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0772`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
