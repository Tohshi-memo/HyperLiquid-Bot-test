# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T10:37:27.737327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0346` n `12`; crypto_alt avg `0.0123` n `230`; crypto_major avg `-0.0003` n `8`; equity avg `0.0222` n `98`; fx avg `0.0078` n `6`; index avg `-0.0066` n `25`; metal avg `-0.0272` n `20`; unknown avg `-0.0071` n `770`
- 1h: commodity avg `0.1186` n `12`; crypto_alt avg `0.1468` n `230`; crypto_major avg `0.101` n `8`; equity avg `0.1909` n `98`; fx avg `0.0234` n `6`; index avg `0.0168` n `25`; metal avg `0.0105` n `20`; unknown avg `-0.0189` n `770`
- 4h: commodity avg `-0.5385` n `12`; crypto_alt avg `1.1953` n `230`; crypto_major avg `0.8843` n `8`; equity avg `0.8082` n `98`; fx avg `0.0438` n `6`; index avg `0.1583` n `25`; metal avg `0.2122` n `20`; unknown avg `0.1084` n `763`
- 24h: crypto_alt avg `0.3694` n `225`; crypto_major avg `-0.222` n `7`; metal avg `0.2921` n `1`; unknown avg `-0.0965` n `679`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.094`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0854`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0789`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
