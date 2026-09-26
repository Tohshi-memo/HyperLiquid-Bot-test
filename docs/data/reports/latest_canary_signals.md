# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T02:52:28.779999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0158` n `12`; crypto_alt avg `-0.2039` n `234`; crypto_major avg `-0.0612` n `8`; equity avg `0.0298` n `141`; fx avg `-0.0195` n `6`; index avg `0.0025` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.0587` n `961`
- 1h: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.2851` n `234`; crypto_major avg `-0.2651` n `8`; equity avg `0.0205` n `141`; fx avg `-0.0179` n `6`; index avg `0.0139` n `26`; metal avg `-0.0011` n `20`; unknown avg `15.0051` n `958`
- 4h: commodity avg `0.3049` n `12`; crypto_alt avg `-0.3795` n `234`; crypto_major avg `-0.3815` n `8`; equity avg `-0.14` n `141`; fx avg `-0.0233` n `6`; index avg `-0.0372` n `26`; metal avg `-0.0227` n `20`; unknown avg `1.7958` n `952`
- 24h: commodity avg `0.0913` n `12`; crypto_alt avg `3.4807` n `234`; crypto_major avg `1.4035` n `8`; equity avg `-0.1859` n `141`; fx avg `-0.1522` n `6`; index avg `0.1458` n `26`; metal avg `0.1985` n `20`; unknown avg `1126.3679` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
