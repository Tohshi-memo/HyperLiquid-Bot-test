# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T13:37:27.801116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `0.0009` n `228`; crypto_major avg `0.1336` n `8`; equity avg `0.0939` n `88`; fx avg `0.0158` n `6`; index avg `-0.1112` n `23`; metal avg `0.2217` n `20`; unknown avg `-0.0268` n `765`
- 1h: commodity avg `0.1073` n `12`; crypto_alt avg `0.4213` n `228`; crypto_major avg `0.827` n `8`; equity avg `-0.4815` n `88`; fx avg `-0.024` n `6`; index avg `-0.141` n `23`; metal avg `0.3861` n `20`; unknown avg `0.0102` n `765`
- 4h: commodity avg `0.059` n `12`; crypto_alt avg `0.1375` n `228`; crypto_major avg `-0.1128` n `8`; equity avg `-0.8741` n `88`; fx avg `-0.0347` n `6`; index avg `-0.153` n `23`; metal avg `0.7316` n `20`; unknown avg `-0.2234` n `765`
- 24h: commodity avg `-0.5542` n `12`; crypto_alt avg `1.6816` n `228`; crypto_major avg `1.1935` n `8`; equity avg `-0.2378` n `88`; fx avg `0.0764` n `6`; index avg `-0.2435` n `23`; metal avg `0.2059` n `20`; unknown avg `0.0647` n `743`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
