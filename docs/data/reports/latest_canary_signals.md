# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T22:37:34.808554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `0.2426` n `230`; crypto_major avg `0.182` n `8`; equity avg `0.0387` n `100`; fx avg `-0.0014` n `6`; index avg `0.0049` n `25`; metal avg `0.0023` n `20`; unknown avg `0.1327` n `774`
- 1h: commodity avg `-0.0783` n `12`; crypto_alt avg `-0.082` n `230`; crypto_major avg `0.0242` n `8`; equity avg `-0.0445` n `100`; fx avg `0.0103` n `6`; index avg `-0.016` n `25`; metal avg `0.009` n `20`; unknown avg `-0.0671` n `774`
- 4h: commodity avg `0.2809` n `12`; crypto_alt avg `-0.0412` n `230`; crypto_major avg `-0.0148` n `8`; equity avg `-0.1361` n `100`; fx avg `-0.0087` n `6`; index avg `-0.0263` n `25`; metal avg `-0.0176` n `20`; unknown avg `-0.1537` n `773`
- 24h: commodity avg `-0.2945` n `12`; crypto_alt avg `-1.0243` n `230`; crypto_major avg `-1.1169` n `8`; equity avg `-3.1988` n `100`; fx avg `-0.1626` n `6`; index avg `-0.4276` n `25`; metal avg `-0.0068` n `20`; unknown avg `14.0219` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1266`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1221`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1124`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.11`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
