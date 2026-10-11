# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T09:37:32.361369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `13`; crypto_alt avg `-0.0058` n `235`; crypto_major avg `0.0019` n `8`; equity avg `-0.0007` n `150`; fx avg `-0.0005` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0034` n `20`; unknown avg `-0.0002` n `1117`
- 1h: commodity avg `0.0011` n `13`; crypto_alt avg `-0.1312` n `235`; crypto_major avg `-0.0143` n `8`; equity avg `0.0387` n `150`; fx avg `0.0007` n `6`; index avg `0.0038` n `26`; metal avg `-0.0047` n `20`; unknown avg `0.0138` n `1115`
- 4h: commodity avg `0.0607` n `13`; crypto_alt avg `0.3844` n `235`; crypto_major avg `-0.0583` n `8`; equity avg `0.0418` n `150`; fx avg `0.001` n `6`; index avg `0.0072` n `26`; metal avg `0.0122` n `20`; unknown avg `0.147` n `1083`
- 24h: commodity avg `0.3655` n `13`; crypto_alt avg `1.0752` n `235`; crypto_major avg `-0.2375` n `8`; equity avg `0.0925` n `150`; fx avg `-0.0005` n `6`; index avg `-0.0052` n `26`; metal avg `0.0098` n `20`; unknown avg `0.6308` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
