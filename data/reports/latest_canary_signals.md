# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T10:52:33.019655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0717` n `12`; crypto_alt avg `0.0309` n `232`; crypto_major avg `-0.0114` n `8`; equity avg `-0.003` n `133`; fx avg `0.0018` n `6`; index avg `0.0105` n `26`; metal avg `0.0337` n `20`; unknown avg `0.0255` n `793`
- 1h: commodity avg `-0.0982` n `12`; crypto_alt avg `-0.1731` n `232`; crypto_major avg `0.0769` n `8`; equity avg `0.0978` n `133`; fx avg `-0.0219` n `6`; index avg `0.0336` n `26`; metal avg `0.0399` n `20`; unknown avg `0.0051` n `791`
- 4h: commodity avg `-0.1411` n `12`; crypto_alt avg `0.9218` n `232`; crypto_major avg `0.4916` n `8`; equity avg `0.5569` n `133`; fx avg `-0.0` n `6`; index avg `0.0741` n `26`; metal avg `0.1149` n `20`; unknown avg `0.0159` n `785`
- 24h: commodity avg `-0.6404` n `12`; crypto_alt avg `2.6869` n `232`; crypto_major avg `4.3212` n `8`; equity avg `2.4589` n `133`; fx avg `-0.0104` n `6`; index avg `0.4657` n `26`; metal avg `0.5215` n `20`; unknown avg `2.1397` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
