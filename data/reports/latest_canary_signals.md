# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T11:52:31.846232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `-0.0894` n `232`; crypto_major avg `-0.0263` n `8`; equity avg `-0.0052` n `133`; fx avg `-0.0052` n `6`; index avg `-0.0111` n `26`; metal avg `0.0384` n `20`; unknown avg `-0.0956` n `793`
- 1h: commodity avg `0.0835` n `12`; crypto_alt avg `0.3347` n `232`; crypto_major avg `0.2528` n `8`; equity avg `0.0044` n `133`; fx avg `-0.0081` n `6`; index avg `-0.0081` n `26`; metal avg `0.0021` n `20`; unknown avg `-0.0049` n `791`
- 4h: commodity avg `0.0608` n `12`; crypto_alt avg `1.013` n `232`; crypto_major avg `0.7041` n `8`; equity avg `0.3159` n `133`; fx avg `-0.0455` n `6`; index avg `0.0354` n `26`; metal avg `-0.0778` n `20`; unknown avg `-0.1272` n `785`
- 24h: commodity avg `-0.5596` n `12`; crypto_alt avg `2.6387` n `232`; crypto_major avg `3.992` n `8`; equity avg `2.4285` n `133`; fx avg `-0.0016` n `6`; index avg `0.4495` n `26`; metal avg `0.4627` n `20`; unknown avg `2.1737` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
