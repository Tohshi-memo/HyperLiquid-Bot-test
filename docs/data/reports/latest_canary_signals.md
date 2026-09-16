# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T08:22:33.370044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0717` n `12`; crypto_alt avg `0.0697` n `234`; crypto_major avg `0.0676` n `8`; equity avg `0.0926` n `137`; fx avg `0.0042` n `6`; index avg `0.0173` n `27`; metal avg `0.0384` n `20`; unknown avg `0.142` n `919`
- 1h: commodity avg `-0.0227` n `12`; crypto_alt avg `-0.3796` n `234`; crypto_major avg `-0.4383` n `8`; equity avg `-0.1245` n `137`; fx avg `0.0154` n `6`; index avg `-0.0144` n `27`; metal avg `-0.0617` n `20`; unknown avg `0.4138` n `917`
- 4h: commodity avg `-0.0563` n `12`; crypto_alt avg `-0.9759` n `234`; crypto_major avg `-0.8223` n `8`; equity avg `0.0464` n `137`; fx avg `-0.0052` n `6`; index avg `0.0137` n `27`; metal avg `-0.0459` n `20`; unknown avg `5.8238` n `881`
- 24h: commodity avg `-0.017` n `12`; crypto_alt avg `-3.0963` n `234`; crypto_major avg `-2.9023` n `8`; equity avg `0.1944` n `137`; fx avg `0.0846` n `6`; index avg `0.1457` n `27`; metal avg `0.6023` n `20`; unknown avg `18889.5653` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
