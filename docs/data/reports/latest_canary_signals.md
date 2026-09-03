# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T06:37:25.740034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `-0.0117` n `232`; crypto_major avg `0.021` n `8`; equity avg `0.0045` n `133`; fx avg `-0.0021` n `6`; index avg `-0.015` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.0081` n `790`
- 1h: commodity avg `0.0303` n `12`; crypto_alt avg `0.3407` n `232`; crypto_major avg `0.3635` n `8`; equity avg `0.2173` n `133`; fx avg `-0.0499` n `6`; index avg `0.0406` n `26`; metal avg `0.0205` n `20`; unknown avg `14.9106` n `754`
- 4h: commodity avg `-0.2434` n `12`; crypto_alt avg `0.4105` n `232`; crypto_major avg `0.0718` n `8`; equity avg `-0.1885` n `133`; fx avg `-0.0596` n `6`; index avg `-0.0789` n `26`; metal avg `0.0276` n `20`; unknown avg `-0.0721` n `754`
- 24h: commodity avg `-0.0165` n `12`; crypto_alt avg `0.6868` n `232`; crypto_major avg `0.5622` n `8`; equity avg `1.2127` n `133`; fx avg `-0.3444` n `6`; index avg `0.1295` n `26`; metal avg `0.7309` n `20`; unknown avg `-0.3398` n `735`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0393`, n `668`, weak_sample_signal
