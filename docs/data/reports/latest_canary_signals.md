# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T14:37:30.283130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `12`; crypto_alt avg `-0.0255` n `230`; crypto_major avg `-0.0974` n `8`; equity avg `-0.0003` n `100`; fx avg `-0.0025` n `6`; index avg `-0.0125` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.0024` n `775`
- 1h: commodity avg `-0.0152` n `12`; crypto_alt avg `0.0413` n `230`; crypto_major avg `0.1203` n `8`; equity avg `0.0479` n `100`; fx avg `-0.0011` n `6`; index avg `0.0025` n `25`; metal avg `0.005` n `20`; unknown avg `0.2076` n `775`
- 4h: commodity avg `0.0475` n `12`; crypto_alt avg `-0.2149` n `230`; crypto_major avg `-0.1247` n `8`; equity avg `0.1057` n `100`; fx avg `-0.0005` n `6`; index avg `-0.0092` n `25`; metal avg `0.0389` n `20`; unknown avg `-0.0664` n `775`
- 24h: commodity avg `-0.4176` n `12`; crypto_alt avg `1.1665` n `230`; crypto_major avg `1.3656` n `8`; equity avg `0.8164` n `100`; fx avg `0.0189` n `6`; index avg `0.1622` n `25`; metal avg `0.1834` n `20`; unknown avg `0.443` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
