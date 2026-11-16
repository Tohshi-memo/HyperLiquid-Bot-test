# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T06:07:33.313989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `13`; crypto_alt avg `-0.0718` n `239`; crypto_major avg `-0.0807` n `8`; equity avg `-0.1021` n `162`; fx avg `0.0031` n `6`; index avg `0.0088` n `27`; metal avg `0.0576` n `20`; unknown avg `-0.1691` n `1243`
- 1h: commodity avg `0.0611` n `13`; crypto_alt avg `-0.3377` n `239`; crypto_major avg `-0.2621` n `8`; equity avg `-0.4851` n `162`; fx avg `-0.0098` n `6`; index avg `-0.0291` n `27`; metal avg `-0.0333` n `20`; unknown avg `-0.1218` n `1241`
- 4h: commodity avg `0.0948` n `13`; crypto_alt avg `-0.2935` n `239`; crypto_major avg `-0.6507` n `8`; equity avg `-1.2532` n `162`; fx avg `-0.0481` n `6`; index avg `-0.1447` n `27`; metal avg `-0.143` n `20`; unknown avg `-0.1968` n `1225`
- 24h: commodity avg `-0.2968` n `13`; crypto_alt avg `-0.1474` n `239`; crypto_major avg `0.5643` n `8`; equity avg `-0.5408` n `162`; fx avg `-0.068` n `6`; index avg `-0.0389` n `27`; metal avg `0.1619` n `20`; unknown avg `187.0029` n `1127`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
