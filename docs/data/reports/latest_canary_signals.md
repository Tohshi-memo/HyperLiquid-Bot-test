# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T21:52:26.167125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9223` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6015` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.0252` n `234`; crypto_major avg `-0.007` n `8`; equity avg `0.0116` n `137`; fx avg `0.0194` n `6`; index avg `0.0069` n `27`; metal avg `-0.0156` n `20`; unknown avg `-0.0869` n `919`
- 1h: commodity avg `0.0061` n `12`; crypto_alt avg `0.1104` n `234`; crypto_major avg `-0.2457` n `8`; equity avg `0.1713` n `137`; fx avg `-0.0158` n `6`; index avg `0.0103` n `27`; metal avg `-0.0025` n `20`; unknown avg `3.1525` n `917`
- 4h: commodity avg `0.0361` n `12`; crypto_alt avg `2.1459` n `234`; crypto_major avg `1.4311` n `8`; equity avg `-0.1704` n `137`; fx avg `0.0658` n `6`; index avg `-0.1654` n `27`; metal avg `-0.4912` n `20`; unknown avg `5.3646` n `829`
- 24h: commodity avg `-0.5885` n `12`; crypto_alt avg `0.5807` n `234`; crypto_major avg `0.9046` n `8`; equity avg `1.0496` n `137`; fx avg `0.0941` n `6`; index avg `0.0357` n `27`; metal avg `-0.293` n `20`; unknown avg `4.5775` n `779`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
