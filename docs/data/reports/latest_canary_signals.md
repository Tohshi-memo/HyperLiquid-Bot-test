# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T05:37:27.500248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `13`; crypto_alt avg `-0.1566` n `236`; crypto_major avg `-0.0721` n `8`; equity avg `-0.0062` n `151`; fx avg `0.0` n `6`; index avg `0.0064` n `26`; metal avg `-0.0086` n `20`; unknown avg `0.1526` n `1193`
- 1h: commodity avg `-0.0075` n `13`; crypto_alt avg `-0.3403` n `236`; crypto_major avg `-0.0476` n `8`; equity avg `0.066` n `151`; fx avg `-0.0005` n `6`; index avg `0.0293` n `26`; metal avg `-0.0186` n `20`; unknown avg `4.0597` n `1191`
- 4h: commodity avg `0.0085` n `13`; crypto_alt avg `0.3565` n `236`; crypto_major avg `0.245` n `8`; equity avg `0.1694` n `151`; fx avg `0.0035` n `6`; index avg `0.0465` n `26`; metal avg `0.0011` n `20`; unknown avg `0.2513` n `1183`
- 24h: commodity avg `0.6467` n `13`; crypto_alt avg `-1.436` n `236`; crypto_major avg `-1.131` n `8`; equity avg `-4.0529` n `151`; fx avg `0.0132` n `6`; index avg `-0.6409` n `26`; metal avg `-0.231` n `20`; unknown avg `40.6352` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1763`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1143`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0767`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
