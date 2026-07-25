# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T05:52:29.935233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `0.0159` n `230`; crypto_major avg `-0.0571` n `8`; equity avg `-0.0039` n `100`; fx avg `-0.0102` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.0324` n `774`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `-0.2068` n `230`; crypto_major avg `-0.2379` n `8`; equity avg `-0.0575` n `100`; fx avg `-0.0071` n `6`; index avg `-0.0075` n `25`; metal avg `-0.0056` n `20`; unknown avg `2.6462` n `774`
- 4h: commodity avg `-0.1545` n `12`; crypto_alt avg `-0.1162` n `230`; crypto_major avg `-0.1669` n `8`; equity avg `0.1929` n `100`; fx avg `-0.0378` n `6`; index avg `0.0404` n `25`; metal avg `-0.015` n `20`; unknown avg `-0.0492` n `774`
- 24h: commodity avg `-0.3894` n `12`; crypto_alt avg `-1.3071` n `230`; crypto_major avg `-1.1774` n `8`; equity avg `-2.4283` n `100`; fx avg `-0.076` n `6`; index avg `-0.1823` n `25`; metal avg `0.1975` n `20`; unknown avg `13.7116` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1149`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1032`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1031`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
