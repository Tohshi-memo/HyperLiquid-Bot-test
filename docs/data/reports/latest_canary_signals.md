# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T19:07:29.257626+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.045` n `12`; crypto_alt avg `0.0407` n `230`; crypto_major avg `-0.022` n `8`; equity avg `-0.013` n `100`; fx avg `0.016` n `6`; index avg `-0.0107` n `25`; metal avg `0.008` n `20`; unknown avg `0.0127` n `774`
- 1h: commodity avg `0.0736` n `12`; crypto_alt avg `-0.1274` n `230`; crypto_major avg `-0.0549` n `8`; equity avg `0.005` n `100`; fx avg `0.014` n `6`; index avg `-0.0164` n `25`; metal avg `0.0095` n `20`; unknown avg `-0.0026` n `774`
- 4h: commodity avg `-0.0573` n `12`; crypto_alt avg `0.6169` n `230`; crypto_major avg `0.8724` n `8`; equity avg `0.1707` n `100`; fx avg `-0.0159` n `6`; index avg `0.0364` n `25`; metal avg `0.0115` n `20`; unknown avg `0.1783` n `774`
- 24h: commodity avg `-0.4282` n `12`; crypto_alt avg `0.5656` n `230`; crypto_major avg `1.2602` n `8`; equity avg `0.3863` n `100`; fx avg `-0.0134` n `6`; index avg `0.116` n `25`; metal avg `0.0312` n `20`; unknown avg `-0.3194` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1305`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1144`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1128`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
