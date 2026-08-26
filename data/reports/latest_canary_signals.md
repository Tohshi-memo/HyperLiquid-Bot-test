# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T14:07:26.465240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0428` n `12`; crypto_alt avg `0.5265` n `231`; crypto_major avg `0.5002` n `8`; equity avg `0.0206` n `122`; fx avg `-0.0068` n `6`; index avg `-0.0098` n `25`; metal avg `-0.0146` n `20`; unknown avg `0.1413` n `797`
- 1h: commodity avg `0.1065` n `12`; crypto_alt avg `-0.0918` n `231`; crypto_major avg `0.1903` n `8`; equity avg `0.6756` n `122`; fx avg `0.0042` n `6`; index avg `0.0883` n `25`; metal avg `0.0103` n `20`; unknown avg `0.0035` n `797`
- 4h: commodity avg `0.3051` n `12`; crypto_alt avg `0.2383` n `231`; crypto_major avg `0.2435` n `8`; equity avg `0.1633` n `122`; fx avg `-0.0062` n `6`; index avg `0.0428` n `25`; metal avg `-0.0819` n `20`; unknown avg `0.0269` n `797`
- 24h: commodity avg `0.0897` n `12`; crypto_alt avg `-1.0471` n `231`; crypto_major avg `-0.7928` n `8`; equity avg `0.3194` n `122`; fx avg `-0.0641` n `6`; index avg `0.068` n `25`; metal avg `0.1236` n `20`; unknown avg `0.5889` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1851`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
