# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T19:52:26.578647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `-0.1018` n `228`; crypto_major avg `-0.0553` n `8`; equity avg `0.0542` n `88`; fx avg `-0.0037` n `6`; index avg `0.0027` n `23`; metal avg `-0.0409` n `20`; unknown avg `1.2905` n `763`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.1308` n `228`; crypto_major avg `0.0898` n `8`; equity avg `0.1601` n `88`; fx avg `-0.0043` n `6`; index avg `-0.0185` n `23`; metal avg `-0.1607` n `20`; unknown avg `1.1103` n `763`
- 4h: commodity avg `-0.0815` n `12`; crypto_alt avg `-0.0116` n `228`; crypto_major avg `0.5459` n `8`; equity avg `0.7596` n `88`; fx avg `-0.0252` n `6`; index avg `0.0435` n `23`; metal avg `-0.0918` n `20`; unknown avg `1.1008` n `763`
- 24h: commodity avg `0.1319` n `12`; crypto_alt avg `-2.3317` n `228`; crypto_major avg `-2.4316` n `8`; equity avg `1.2798` n `88`; fx avg `0.1387` n `6`; index avg `0.2756` n `23`; metal avg `0.1739` n `20`; unknown avg `8.0398` n `733`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0525`, n `668`, weak_sample_signal
