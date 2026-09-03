# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T20:52:28.830648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `12`; crypto_alt avg `0.0956` n `232`; crypto_major avg `0.0075` n `8`; equity avg `-0.0395` n `133`; fx avg `0.0046` n `6`; index avg `-0.0042` n `26`; metal avg `0.0067` n `20`; unknown avg `-0.2901` n `792`
- 1h: commodity avg `0.0499` n `12`; crypto_alt avg `-0.0402` n `232`; crypto_major avg `-0.1539` n `8`; equity avg `-0.0227` n `133`; fx avg `0.0062` n `6`; index avg `-0.0147` n `26`; metal avg `-0.0252` n `20`; unknown avg `-0.0992` n `778`
- 4h: commodity avg `0.0336` n `12`; crypto_alt avg `0.278` n `232`; crypto_major avg `0.3655` n `8`; equity avg `0.0938` n `133`; fx avg `0.0194` n `6`; index avg `0.011` n `26`; metal avg `-0.0431` n `20`; unknown avg `4.3022` n `778`
- 24h: commodity avg `-0.0557` n `12`; crypto_alt avg `4.2846` n `232`; crypto_major avg `5.3126` n `8`; equity avg `1.478` n `133`; fx avg `-0.2265` n `6`; index avg `0.1995` n `26`; metal avg `0.7602` n `20`; unknown avg `25.6543` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
