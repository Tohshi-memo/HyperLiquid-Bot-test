# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T03:37:28.810822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0397` n `12`; crypto_alt avg `-0.0117` n `234`; crypto_major avg `0.0895` n `8`; equity avg `0.0877` n `142`; fx avg `-0.0052` n `6`; index avg `0.0334` n `26`; metal avg `-0.0117` n `20`; unknown avg `0.7886` n `963`
- 1h: commodity avg `0.0228` n `12`; crypto_alt avg `-0.1539` n `234`; crypto_major avg `-0.0222` n `8`; equity avg `0.1755` n `142`; fx avg `0.0212` n `6`; index avg `0.053` n `26`; metal avg `0.0216` n `20`; unknown avg `3.6378` n `961`
- 4h: commodity avg `0.0677` n `12`; crypto_alt avg `0.2077` n `234`; crypto_major avg `-0.0191` n `8`; equity avg `-0.2458` n `142`; fx avg `-0.0375` n `6`; index avg `-0.0373` n `26`; metal avg `-0.0938` n `20`; unknown avg `1.9517` n `955`
- 24h: commodity avg `-0.9509` n `12`; crypto_alt avg `1.4524` n `234`; crypto_major avg `0.2334` n `8`; equity avg `0.9697` n `142`; fx avg `-0.1716` n `6`; index avg `0.1438` n `26`; metal avg `0.1933` n `20`; unknown avg `3245.7131` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
