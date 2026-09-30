# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T23:07:29.531857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `-0.0348` n `234`; crypto_major avg `-0.044` n `8`; equity avg `-0.0203` n `142`; fx avg `0.0029` n `6`; index avg `-0.003` n `26`; metal avg `-0.0164` n `20`; unknown avg `0.2775` n `973`
- 1h: commodity avg `-0.0202` n `12`; crypto_alt avg `0.9817` n `234`; crypto_major avg `0.3433` n `8`; equity avg `0.1878` n `142`; fx avg `-0.0009` n `6`; index avg `0.0519` n `26`; metal avg `-0.034` n `20`; unknown avg `0.0558` n `973`
- 4h: commodity avg `-0.1107` n `12`; crypto_alt avg `0.3454` n `234`; crypto_major avg `0.2157` n `8`; equity avg `-0.1011` n `142`; fx avg `0.0266` n `6`; index avg `-0.0121` n `26`; metal avg `0.0095` n `20`; unknown avg `1.2622` n `887`
- 24h: commodity avg `0.1505` n `12`; crypto_alt avg `0.2112` n `234`; crypto_major avg `0.6339` n `8`; equity avg `-0.3452` n `142`; fx avg `0.0822` n `6`; index avg `-0.0188` n `26`; metal avg `-0.2737` n `20`; unknown avg `763.4927` n `813`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
