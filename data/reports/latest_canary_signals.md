# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T04:07:26.570692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `0.2108` n `228`; crypto_major avg `0.2841` n `8`; equity avg `0.0281` n `88`; fx avg `-0.0021` n `6`; index avg `0.0128` n `23`; metal avg `0.0097` n `20`; unknown avg `-0.1101` n `764`
- 1h: commodity avg `0.0274` n `12`; crypto_alt avg `0.091` n `228`; crypto_major avg `0.3818` n `8`; equity avg `-0.0003` n `88`; fx avg `-0.0035` n `6`; index avg `0.003` n `23`; metal avg `0.0032` n `20`; unknown avg `9.9554` n `764`
- 4h: commodity avg `-0.0586` n `12`; crypto_alt avg `0.111` n `228`; crypto_major avg `0.2084` n `8`; equity avg `0.0978` n `88`; fx avg `0.0094` n `6`; index avg `0.023` n `23`; metal avg `0.0012` n `20`; unknown avg `0.6288` n `764`
- 24h: commodity avg `-0.0459` n `12`; crypto_alt avg `2.1477` n `228`; crypto_major avg `1.9817` n `8`; equity avg `1.7797` n `87`; fx avg `-0.0265` n `6`; index avg `0.1463` n `23`; metal avg `1.2659` n `20`; unknown avg `0.0272` n `716`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.211`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2061`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
