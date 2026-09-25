# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T16:52:34.087564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0451` n `12`; crypto_alt avg `-0.0959` n `234`; crypto_major avg `-0.0998` n `8`; equity avg `-0.0706` n `141`; fx avg `-0.0086` n `6`; index avg `-0.0216` n `26`; metal avg `-0.022` n `20`; unknown avg `1.3426` n `960`
- 1h: commodity avg `-0.3457` n `12`; crypto_alt avg `1.0578` n `234`; crypto_major avg `0.7357` n `8`; equity avg `0.5909` n `141`; fx avg `-0.0106` n `6`; index avg `0.1427` n `26`; metal avg `0.1211` n `20`; unknown avg `2.2594` n `942`
- 4h: commodity avg `-0.2787` n `12`; crypto_alt avg `-0.1092` n `234`; crypto_major avg `-0.7863` n `8`; equity avg `-0.5379` n `141`; fx avg `-0.062` n `6`; index avg `0.0342` n `26`; metal avg `0.0064` n `20`; unknown avg `9.4449` n `894`
- 24h: commodity avg `-0.6972` n `12`; crypto_alt avg `1.5698` n `234`; crypto_major avg `0.5204` n `8`; equity avg `0.1312` n `141`; fx avg `-0.2343` n `6`; index avg `0.1319` n `26`; metal avg `0.0992` n `20`; unknown avg `1603.1729` n `805`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
