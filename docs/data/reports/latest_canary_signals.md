# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T17:37:26.762949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `0.1423` n `230`; crypto_major avg `0.1647` n `8`; equity avg `0.1937` n `100`; fx avg `-0.0028` n `6`; index avg `0.0371` n `25`; metal avg `0.0454` n `20`; unknown avg `0.0336` n `773`
- 1h: commodity avg `0.0655` n `12`; crypto_alt avg `0.3756` n `230`; crypto_major avg `0.2561` n `8`; equity avg `-0.1533` n `100`; fx avg `-0.0309` n `6`; index avg `-0.0303` n `25`; metal avg `-0.0216` n `20`; unknown avg `0.0124` n `773`
- 4h: commodity avg `-0.324` n `12`; crypto_alt avg `0.3643` n `230`; crypto_major avg `0.1004` n `8`; equity avg `-1.0156` n `100`; fx avg `-0.0087` n `6`; index avg `-0.0218` n `25`; metal avg `0.1613` n `20`; unknown avg `13.2828` n `773`
- 24h: commodity avg `-0.66` n `12`; crypto_alt avg `-0.9913` n `230`; crypto_major avg `-0.8902` n `8`; equity avg `-2.4215` n `100`; fx avg `-0.1555` n `6`; index avg `-0.2227` n `25`; metal avg `0.1544` n `20`; unknown avg `14.0632` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1204`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1179`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1093`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1034`, n `666`, weak_sample_signal
