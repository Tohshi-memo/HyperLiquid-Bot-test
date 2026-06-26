# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T04:52:25.747274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `-0.0325` n `228`; crypto_major avg `-0.0758` n `8`; equity avg `-0.1347` n `86`; fx avg `-0.007` n `6`; index avg `-0.0357` n `23`; metal avg `0.0163` n `20`; unknown avg `1.364` n `765`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `-0.138` n `228`; crypto_major avg `-0.2022` n `8`; equity avg `-0.0685` n `86`; fx avg `-0.0153` n `6`; index avg `-0.0208` n `23`; metal avg `0.0199` n `20`; unknown avg `1.687` n `765`
- 4h: commodity avg `-0.2248` n `12`; crypto_alt avg `-0.7048` n `228`; crypto_major avg `-0.5831` n `8`; equity avg `-1.8608` n `86`; fx avg `-0.0175` n `6`; index avg `-0.4403` n `23`; metal avg `-0.4932` n `20`; unknown avg `-0.1042` n `749`
- 24h: commodity avg `0.2752` n `12`; crypto_alt avg `-2.0367` n `228`; crypto_major avg `-2.0633` n `8`; equity avg `-4.3227` n `86`; fx avg `0.0287` n `6`; index avg `-0.7358` n `23`; metal avg `-0.1551` n `20`; unknown avg `0.6759` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
