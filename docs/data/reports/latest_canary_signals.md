# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T22:52:27.366056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `0.1375` n `234`; crypto_major avg `0.12` n `8`; equity avg `0.0105` n `141`; fx avg `0.0047` n `6`; index avg `-0.0036` n `26`; metal avg `0.0118` n `20`; unknown avg `2.4052` n `960`
- 1h: commodity avg `-0.0104` n `12`; crypto_alt avg `1.0967` n `234`; crypto_major avg `0.7468` n `8`; equity avg `0.0086` n `141`; fx avg `0.0022` n `6`; index avg `-0.0057` n `26`; metal avg `-0.0075` n `20`; unknown avg `0.5759` n `932`
- 4h: commodity avg `0.1933` n `12`; crypto_alt avg `0.7059` n `234`; crypto_major avg `0.459` n `8`; equity avg `-0.0087` n `141`; fx avg `-0.0063` n `6`; index avg `0.0244` n `26`; metal avg `-0.0409` n `20`; unknown avg `0.1163` n `852`
- 24h: commodity avg `-0.4473` n `12`; crypto_alt avg `3.1862` n `234`; crypto_major avg `1.5569` n `8`; equity avg `0.135` n `141`; fx avg `-0.2232` n `6`; index avg `0.259` n `26`; metal avg `0.1731` n `20`; unknown avg `1124.9573` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
