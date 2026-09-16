# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T03:37:28.198911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0655` n `12`; crypto_alt avg `-0.2724` n `234`; crypto_major avg `-0.3038` n `8`; equity avg `-0.0865` n `137`; fx avg `-0.0025` n `6`; index avg `-0.032` n `27`; metal avg `-0.0723` n `20`; unknown avg `1.2666` n `919`
- 1h: commodity avg `0.0052` n `12`; crypto_alt avg `-0.1135` n `234`; crypto_major avg `-0.2138` n `8`; equity avg `0.3038` n `137`; fx avg `0.0134` n `6`; index avg `0.033` n `27`; metal avg `0.0721` n `20`; unknown avg `0.5071` n `913`
- 4h: commodity avg `-0.1335` n `12`; crypto_alt avg `-0.2571` n `234`; crypto_major avg `0.2448` n `8`; equity avg `0.5497` n `137`; fx avg `0.0776` n `6`; index avg `0.0761` n `27`; metal avg `0.2501` n `20`; unknown avg `5.494` n `907`
- 24h: commodity avg `0.2384` n `12`; crypto_alt avg `-3.5866` n `234`; crypto_major avg `-3.5302` n `8`; equity avg `-0.8549` n `137`; fx avg `0.2238` n `6`; index avg `-0.0664` n `27`; metal avg `0.2956` n `20`; unknown avg `0.7573` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
