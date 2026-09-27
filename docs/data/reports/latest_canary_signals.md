# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T14:53:22.617500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `12`; crypto_alt avg `-0.1837` n `234`; crypto_major avg `-0.1078` n `8`; equity avg `0.0162` n `141`; fx avg `-0.0008` n `6`; index avg `0.0042` n `26`; metal avg `-0.0034` n `20`; unknown avg `3.2835` n `962`
- 1h: commodity avg `0.0034` n `12`; crypto_alt avg `-0.3489` n `234`; crypto_major avg `-0.5458` n `8`; equity avg `-0.0702` n `141`; fx avg `-0.0093` n `6`; index avg `-0.0145` n `26`; metal avg `-0.0103` n `20`; unknown avg `2.4684` n `960`
- 4h: commodity avg `-0.0157` n `12`; crypto_alt avg `-1.1179` n `234`; crypto_major avg `-0.8467` n `8`; equity avg `-0.0893` n `141`; fx avg `0.0002` n `6`; index avg `-0.0333` n `26`; metal avg `-0.0182` n `20`; unknown avg `7.4347` n `954`
- 24h: commodity avg `-0.0291` n `12`; crypto_alt avg `-0.7886` n `234`; crypto_major avg `-0.2607` n `8`; equity avg `0.1826` n `141`; fx avg `-0.0359` n `6`; index avg `-0.0038` n `26`; metal avg `-0.0259` n `20`; unknown avg `224.8342` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
