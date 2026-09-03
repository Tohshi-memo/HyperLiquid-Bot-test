# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T23:31:06.294734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `0.0441` n `232`; crypto_major avg `-0.0407` n `8`; equity avg `0.0271` n `133`; fx avg `-0.0213` n `6`; index avg `-0.0015` n `26`; metal avg `0.0144` n `20`; unknown avg `-0.169` n `792`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `0.1301` n `232`; crypto_major avg `0.2448` n `8`; equity avg `0.0505` n `133`; fx avg `-0.0164` n `6`; index avg `0.0059` n `26`; metal avg `-0.0007` n `20`; unknown avg `1.5642` n `790`
- 4h: commodity avg `0.1067` n `12`; crypto_alt avg `-0.5611` n `232`; crypto_major avg `-0.4871` n `8`; equity avg `-0.0821` n `133`; fx avg `-0.0031` n `6`; index avg `-0.0147` n `26`; metal avg `-0.0195` n `20`; unknown avg `3.021` n `766`
- 24h: commodity avg `-0.0777` n `12`; crypto_alt avg `4.0521` n `232`; crypto_major avg `5.1582` n `8`; equity avg `1.2287` n `133`; fx avg `-0.2372` n `6`; index avg `0.1609` n `26`; metal avg `0.817` n `20`; unknown avg `1.2432` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
