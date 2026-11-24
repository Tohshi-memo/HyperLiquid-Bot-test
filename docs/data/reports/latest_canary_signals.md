# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T04:57:40.610530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0156` n `13`; crypto_alt avg `-0.2101` n `239`; crypto_major avg `-0.382` n `8`; equity avg `-0.1178` n `166`; fx avg `-0.0054` n `6`; index avg `-0.0136` n `27`; metal avg `0.0444` n `20`; unknown avg `0.435` n `1260`
- 1h: commodity avg `-0.0519` n `13`; crypto_alt avg `0.6481` n `239`; crypto_major avg `0.3803` n `8`; equity avg `0.0018` n `166`; fx avg `-0.0011` n `6`; index avg `0.0024` n `27`; metal avg `-0.0233` n `20`; unknown avg `1.3611` n `1242`
- 4h: commodity avg `-0.2026` n `13`; crypto_alt avg `0.0982` n `239`; crypto_major avg `-0.4157` n `8`; equity avg `-0.6427` n `166`; fx avg `-0.023` n `6`; index avg `0.0226` n `27`; metal avg `-0.4943` n `20`; unknown avg `162.2071` n `1238`
- 24h: commodity avg `-1.2834` n `13`; crypto_alt avg `0.6987` n `239`; crypto_major avg `0.2501` n `8`; equity avg `4.6953` n `166`; fx avg `-0.2724` n `6`; index avg `0.6376` n `27`; metal avg `-0.0025` n `20`; unknown avg `244.1741` n `1030`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
