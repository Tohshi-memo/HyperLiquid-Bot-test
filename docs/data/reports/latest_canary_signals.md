# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T21:37:30.689447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.0057` n `234`; crypto_major avg `-0.0183` n `8`; equity avg `0.0648` n `141`; fx avg `-0.0127` n `6`; index avg `0.0147` n `26`; metal avg `0.0191` n `20`; unknown avg `0.5271` n `960`
- 1h: commodity avg `-0.0364` n `12`; crypto_alt avg `-1.0858` n `234`; crypto_major avg `-0.6238` n `8`; equity avg `0.0281` n `141`; fx avg `-0.0255` n `6`; index avg `0.0138` n `26`; metal avg `0.018` n `20`; unknown avg `-0.2085` n `956`
- 4h: commodity avg `0.0393` n `12`; crypto_alt avg `0.3302` n `234`; crypto_major avg `0.0863` n `8`; equity avg `-0.0381` n `141`; fx avg `-0.0294` n `6`; index avg `0.0435` n `26`; metal avg `0.0555` n `20`; unknown avg `-0.0623` n `876`
- 24h: commodity avg `-0.6357` n `12`; crypto_alt avg `1.2395` n `234`; crypto_major avg `0.1463` n `8`; equity avg `0.1121` n `141`; fx avg `-0.2503` n `6`; index avg `0.2564` n `26`; metal avg `0.1954` n `20`; unknown avg `1147.4439` n `794`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
