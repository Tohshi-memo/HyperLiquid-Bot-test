# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T17:07:30.104930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1504` n `13`; crypto_alt avg `1.0351` n `239`; crypto_major avg `1.1749` n `8`; equity avg `1.831` n `168`; fx avg `0.0251` n `6`; index avg `0.2001` n `27`; metal avg `0.4241` n `20`; unknown avg `21.3517` n `1256`
- 1h: commodity avg `0.0222` n `13`; crypto_alt avg `1.5295` n `239`; crypto_major avg `1.3261` n `8`; equity avg `1.8293` n `168`; fx avg `0.041` n `6`; index avg `0.1973` n `27`; metal avg `0.3999` n `20`; unknown avg `26.0756` n `1262`
- 4h: commodity avg `0.2732` n `13`; crypto_alt avg `0.9437` n `239`; crypto_major avg `0.8438` n `8`; equity avg `-0.4358` n `168`; fx avg `0.0793` n `6`; index avg `-0.0335` n `27`; metal avg `-0.2522` n `20`; unknown avg `43.5969` n `1241`
- 24h: commodity avg `0.472` n `13`; crypto_alt avg `-0.2588` n `239`; crypto_major avg `-1.0347` n `8`; equity avg `-3.7478` n `168`; fx avg `-0.0152` n `6`; index avg `-0.3935` n `27`; metal avg `-0.6929` n `20`; unknown avg `643.2616` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
