# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T06:22:22.782446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0867` n `13`; crypto_alt avg `-0.0777` n `239`; crypto_major avg `-0.0302` n `8`; equity avg `-0.0754` n `162`; fx avg `0.0019` n `6`; index avg `-0.0194` n `27`; metal avg `0.0666` n `20`; unknown avg `7.0914` n `1263`
- 1h: commodity avg `0.1616` n `13`; crypto_alt avg `-0.5801` n `239`; crypto_major avg `-0.6556` n `8`; equity avg `-0.7615` n `162`; fx avg `-0.0031` n `6`; index avg `-0.0726` n `27`; metal avg `-0.0807` n `20`; unknown avg `-0.1054` n `1241`
- 4h: commodity avg `0.2026` n `13`; crypto_alt avg `-0.9598` n `239`; crypto_major avg `-1.0801` n `8`; equity avg `-1.5019` n `162`; fx avg `-0.0498` n `6`; index avg `-0.1764` n `27`; metal avg `-0.0905` n `20`; unknown avg `-0.0453` n `1231`
- 24h: commodity avg `-0.2108` n `13`; crypto_alt avg `-0.3199` n `239`; crypto_major avg `0.3601` n `8`; equity avg `-0.6328` n `162`; fx avg `-0.0676` n `6`; index avg `-0.0595` n `27`; metal avg `0.2047` n `20`; unknown avg `0.4329` n `1127`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
