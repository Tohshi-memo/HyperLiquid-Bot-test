# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T06:37:30.776243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `0.0922` n `234`; crypto_major avg `-0.063` n `8`; equity avg `-0.0047` n `141`; fx avg `-0.0022` n `6`; index avg `-0.0017` n `26`; metal avg `0.0042` n `20`; unknown avg `-0.0327` n `961`
- 1h: commodity avg `0.0215` n `12`; crypto_alt avg `0.2956` n `234`; crypto_major avg `-0.0992` n `8`; equity avg `-0.0148` n `141`; fx avg `-0.0082` n `6`; index avg `0.0016` n `26`; metal avg `0.0061` n `20`; unknown avg `-0.1886` n `935`
- 4h: commodity avg `-0.0187` n `12`; crypto_alt avg `0.0881` n `234`; crypto_major avg `-0.6688` n `8`; equity avg `-0.0081` n `141`; fx avg `-0.0121` n `6`; index avg `0.0` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.3339` n `929`
- 24h: commodity avg `0.1252` n `12`; crypto_alt avg `3.4541` n `234`; crypto_major avg `0.9491` n `8`; equity avg `-0.7205` n `141`; fx avg `-0.0975` n `6`; index avg `0.0486` n `26`; metal avg `0.1873` n `20`; unknown avg `1129.7166` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
