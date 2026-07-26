# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T15:07:30.912466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0334` n `12`; crypto_alt avg `0.0002` n `230`; crypto_major avg `0.1371` n `8`; equity avg `0.0192` n `100`; fx avg `-0.0037` n `6`; index avg `0.0029` n `25`; metal avg `-0.011` n `20`; unknown avg `-0.0122` n `775`
- 1h: commodity avg `-0.0818` n `12`; crypto_alt avg `-0.0261` n `230`; crypto_major avg `0.0375` n `8`; equity avg `0.0009` n `100`; fx avg `-0.0045` n `6`; index avg `-0.0057` n `25`; metal avg `-0.023` n `20`; unknown avg `0.0042` n `775`
- 4h: commodity avg `-0.0365` n `12`; crypto_alt avg `-0.0654` n `230`; crypto_major avg `0.179` n `8`; equity avg `0.1001` n `100`; fx avg `-0.0049` n `6`; index avg `0.0092` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.0907` n `775`
- 24h: commodity avg `-0.5012` n `12`; crypto_alt avg `1.1626` n `230`; crypto_major avg `1.3806` n `8`; equity avg `0.8249` n `100`; fx avg `0.0144` n `6`; index avg `0.1791` n `25`; metal avg `0.1608` n `20`; unknown avg `0.4396` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
