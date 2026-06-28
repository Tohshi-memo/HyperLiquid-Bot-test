# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T02:22:26.233655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0195` n `12`; crypto_alt avg `-0.306` n `228`; crypto_major avg `-0.3331` n `8`; equity avg `0.009` n `88`; fx avg `0.008` n `6`; index avg `0.0091` n `23`; metal avg `-0.0017` n `20`; unknown avg `0.1354` n `748`
- 1h: commodity avg `-0.0049` n `12`; crypto_alt avg `-0.0863` n `228`; crypto_major avg `-0.1602` n `8`; equity avg `0.0277` n `88`; fx avg `0.003` n `6`; index avg `0.0197` n `23`; metal avg `0.0152` n `20`; unknown avg `-0.8257` n `748`
- 4h: commodity avg `0.314` n `12`; crypto_alt avg `0.1129` n `228`; crypto_major avg `-0.1734` n `8`; equity avg `-0.0608` n `88`; fx avg `-0.0246` n `6`; index avg `-0.0191` n `23`; metal avg `0.06` n `20`; unknown avg `-0.5` n `748`
- 24h: commodity avg `0.6395` n `12`; crypto_alt avg `-1.1452` n `228`; crypto_major avg `-1.6035` n `8`; equity avg `0.0327` n `88`; fx avg `-0.007` n `6`; index avg `-0.1127` n `23`; metal avg `-0.0454` n `20`; unknown avg `-0.4164` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2154`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
