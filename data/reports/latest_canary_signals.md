# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T23:52:30.238281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0277` n `12`; crypto_alt avg `-0.1187` n `228`; crypto_major avg `-0.0754` n `8`; equity avg `-0.0221` n `78`; fx avg `0.0006` n `6`; index avg `-0.007` n `23`; metal avg `-0.0035` n `18`; unknown avg `-0.1191` n `701`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.1267` n `228`; crypto_major avg `-0.1296` n `8`; equity avg `-0.0175` n `78`; fx avg `-0.001` n `6`; index avg `-0.026` n `23`; metal avg `-0.0072` n `18`; unknown avg `0.1782` n `701`
- 4h: commodity avg `0.0163` n `12`; crypto_alt avg `0.607` n `228`; crypto_major avg `0.7439` n `8`; equity avg `0.1794` n `78`; fx avg `0.1853` n `6`; index avg `0.003` n `23`; metal avg `0.0344` n `18`; unknown avg `-0.5398` n `701`
- 24h: commodity avg `0.2135` n `12`; crypto_alt avg `1.1341` n `228`; crypto_major avg `1.6862` n `8`; equity avg `0.4276` n `78`; fx avg `0.0549` n `6`; index avg `0.0049` n `23`; metal avg `-0.0395` n `18`; unknown avg `-0.3632` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
