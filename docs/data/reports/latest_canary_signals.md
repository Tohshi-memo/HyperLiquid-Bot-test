# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T22:37:27.319124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0419` n `12`; crypto_alt avg `0.1417` n `234`; crypto_major avg `0.2034` n `8`; equity avg `0.085` n `140`; fx avg `-0.0014` n `6`; index avg `0.0203` n `26`; metal avg `0.0223` n `20`; unknown avg `-0.2536` n `943`
- 1h: commodity avg `-0.255` n `12`; crypto_alt avg `0.5854` n `234`; crypto_major avg `0.5666` n `8`; equity avg `0.3055` n `140`; fx avg `0.0812` n `6`; index avg `0.0702` n `26`; metal avg `0.0899` n `20`; unknown avg `-0.0395` n `913`
- 4h: commodity avg `-0.2697` n `12`; crypto_alt avg `0.9341` n `234`; crypto_major avg `0.3838` n `8`; equity avg `0.379` n `140`; fx avg `0.037` n `6`; index avg `0.0823` n `26`; metal avg `0.0866` n `20`; unknown avg `1.0205` n `853`
- 24h: commodity avg `0.0516` n `12`; crypto_alt avg `1.7302` n `234`; crypto_major avg `0.5642` n `8`; equity avg `0.2051` n `140`; fx avg `0.0428` n `6`; index avg `0.0315` n `26`; metal avg `0.0457` n `20`; unknown avg `3.4758` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
