# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T23:37:27.183243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.0085` n `230`; crypto_major avg `0.0178` n `8`; equity avg `0.0378` n `100`; fx avg `-0.0015` n `6`; index avg `0.0002` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.0177` n `774`
- 1h: commodity avg `0.0128` n `12`; crypto_alt avg `-0.1212` n `230`; crypto_major avg `-0.0525` n `8`; equity avg `0.0435` n `100`; fx avg `0.0021` n `6`; index avg `0.0024` n `25`; metal avg `-0.0127` n `20`; unknown avg `-0.0899` n `774`
- 4h: commodity avg `0.0001` n `12`; crypto_alt avg `-0.0684` n `230`; crypto_major avg `-0.1687` n `8`; equity avg `0.1076` n `100`; fx avg `-0.0051` n `6`; index avg `0.0303` n `25`; metal avg `-0.0133` n `20`; unknown avg `-0.166` n `774`
- 24h: commodity avg `-0.6526` n `12`; crypto_alt avg `0.475` n `230`; crypto_major avg `1.0319` n `8`; equity avg `0.6404` n `100`; fx avg `-0.0363` n `6`; index avg `0.1765` n `25`; metal avg `-0.0068` n `20`; unknown avg `-0.2746` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1794`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1348`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1231`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1161`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1151`, n `666`, weak_sample_signal
