# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T23:07:31.639513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.0096` n `230`; crypto_major avg `-0.0986` n `8`; equity avg `-0.0591` n `108`; fx avg `-0.0053` n `6`; index avg `-0.034` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.097` n `782`
- 1h: commodity avg `-0.0042` n `12`; crypto_alt avg `0.0097` n `230`; crypto_major avg `-0.1806` n `8`; equity avg `0.1468` n `108`; fx avg `0.0023` n `6`; index avg `0.0156` n `25`; metal avg `0.0183` n `20`; unknown avg `-0.1327` n `782`
- 4h: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.2081` n `230`; crypto_major avg `-0.6918` n `8`; equity avg `-0.968` n `108`; fx avg `0.0116` n `6`; index avg `-0.1111` n `25`; metal avg `-0.0719` n `20`; unknown avg `-0.0641` n `782`
- 24h: commodity avg `-0.0296` n `12`; crypto_alt avg `0.3324` n `230`; crypto_major avg `0.2723` n `8`; equity avg `-0.7911` n `108`; fx avg `-0.0504` n `6`; index avg `-0.1287` n `25`; metal avg `0.8499` n `20`; unknown avg `0.7247` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
