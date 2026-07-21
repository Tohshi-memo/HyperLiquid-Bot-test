# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T01:13:39.650445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0984` n `12`; crypto_alt avg `0.0409` n `230`; crypto_major avg `0.0396` n `8`; equity avg `0.2137` n `98`; fx avg `0.016` n `6`; index avg `0.0571` n `25`; metal avg `0.0326` n `20`; unknown avg `-0.1834` n `771`
- 1h: commodity avg `-0.0728` n `12`; crypto_alt avg `0.3887` n `230`; crypto_major avg `0.4714` n `8`; equity avg `0.9023` n `98`; fx avg `0.0246` n `6`; index avg `0.2618` n `25`; metal avg `0.2099` n `20`; unknown avg `0.0576` n `771`
- 4h: commodity avg `-0.0601` n `12`; crypto_alt avg `0.1692` n `230`; crypto_major avg `0.1865` n `8`; equity avg `0.5968` n `98`; fx avg `0.0359` n `6`; index avg `0.1162` n `25`; metal avg `0.1377` n `20`; unknown avg `-0.4423` n `770`
- 24h: commodity avg `-0.3732` n `12`; crypto_alt avg `1.7002` n `230`; crypto_major avg `1.4637` n `8`; equity avg `0.0174` n `98`; fx avg `-0.1155` n `6`; index avg `0.0282` n `25`; metal avg `0.1901` n `20`; unknown avg `-0.0554` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0998`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0995`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.086`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
