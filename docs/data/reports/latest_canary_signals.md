# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T04:07:26.034179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `12`; crypto_alt avg `-0.073` n `230`; crypto_major avg `-0.0877` n `8`; equity avg `0.1015` n `96`; fx avg `0.0046` n `6`; index avg `0.0013` n `25`; metal avg `-0.0188` n `20`; unknown avg `-0.0017` n `770`
- 1h: commodity avg `0.016` n `12`; crypto_alt avg `-0.1975` n `230`; crypto_major avg `-0.188` n `8`; equity avg `0.0755` n `96`; fx avg `0.0057` n `6`; index avg `-0.0205` n `25`; metal avg `0.0007` n `20`; unknown avg `0.1056` n `770`
- 4h: commodity avg `-0.0234` n `12`; crypto_alt avg `-0.1708` n `230`; crypto_major avg `0.0232` n `8`; equity avg `0.2466` n `96`; fx avg `0.0535` n `6`; index avg `0.0009` n `25`; metal avg `0.0303` n `20`; unknown avg `-0.5828` n `770`
- 24h: commodity avg `0.3449` n `12`; crypto_alt avg `-0.2354` n `230`; crypto_major avg `0.606` n `8`; equity avg `-0.1012` n `96`; fx avg `-0.0229` n `6`; index avg `-0.035` n `25`; metal avg `-0.027` n `20`; unknown avg `0.0384` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
