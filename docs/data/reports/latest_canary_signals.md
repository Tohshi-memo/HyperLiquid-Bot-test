# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T21:52:31.283746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `13`; crypto_alt avg `-0.0197` n `239`; crypto_major avg `-0.0763` n `8`; equity avg `-0.0127` n `168`; fx avg `-0.002` n `6`; index avg `-0.0053` n `27`; metal avg `0.0017` n `20`; unknown avg `2.8707` n `1263`
- 1h: commodity avg `0.0001` n `13`; crypto_alt avg `0.0922` n `239`; crypto_major avg `0.1359` n `8`; equity avg `0.1786` n `168`; fx avg `-0.0033` n `6`; index avg `0.01` n `27`; metal avg `0.0301` n `20`; unknown avg `121.9454` n `1217`
- 4h: commodity avg `0.0241` n `13`; crypto_alt avg `0.75` n `239`; crypto_major avg `0.9948` n `8`; equity avg `0.5885` n `168`; fx avg `-0.0068` n `6`; index avg `0.0389` n `27`; metal avg `0.056` n `20`; unknown avg `52.9347` n `1183`
- 24h: commodity avg `0.053` n `13`; crypto_alt avg `1.676` n `239`; crypto_major avg `1.1063` n `8`; equity avg `1.5669` n `168`; fx avg `-0.0184` n `6`; index avg `0.1015` n `27`; metal avg `0.1226` n `20`; unknown avg `19.4454` n `1023`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
