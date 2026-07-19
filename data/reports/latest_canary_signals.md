# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T06:52:28.221731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0822` n `12`; crypto_alt avg `0.0117` n `230`; crypto_major avg `-0.0237` n `8`; equity avg `-0.0107` n `96`; fx avg `-0.0031` n `6`; index avg `-0.0059` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0055` n `770`
- 1h: commodity avg `0.0684` n `12`; crypto_alt avg `0.0524` n `230`; crypto_major avg `-0.0119` n `8`; equity avg `-0.0119` n `96`; fx avg `0.0028` n `6`; index avg `0.0045` n `25`; metal avg `0.0108` n `20`; unknown avg `-0.0035` n `752`
- 4h: commodity avg `0.0805` n `12`; crypto_alt avg `-0.0788` n `230`; crypto_major avg `-0.1312` n `8`; equity avg `0.0804` n `96`; fx avg `0.0058` n `6`; index avg `0.0014` n `25`; metal avg `0.024` n `20`; unknown avg `0.0007` n `752`
- 24h: commodity avg `0.36` n `12`; crypto_alt avg `0.2508` n `230`; crypto_major avg `0.9829` n `8`; equity avg `0.0706` n `96`; fx avg `-0.0072` n `6`; index avg `-0.0189` n `25`; metal avg `-0.0048` n `20`; unknown avg `0.0063` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
