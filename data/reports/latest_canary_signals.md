# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T14:52:34.205724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.258` n `12`; crypto_alt avg `-1.6348` n `234`; crypto_major avg `-1.2582` n `8`; equity avg `-0.352` n `141`; fx avg `0.008` n `6`; index avg `-0.042` n `26`; metal avg `-0.0376` n `20`; unknown avg `4.4139` n `943`
- 1h: commodity avg `0.3999` n `12`; crypto_alt avg `0.1668` n `234`; crypto_major avg `-0.2681` n `8`; equity avg `-0.029` n `141`; fx avg `0.0075` n `6`; index avg `-0.0323` n `26`; metal avg `-0.0596` n `20`; unknown avg `4.5762` n `941`
- 4h: commodity avg `0.4486` n `12`; crypto_alt avg `1.9124` n `234`; crypto_major avg `0.7222` n `8`; equity avg `0.1506` n `141`; fx avg `-0.0227` n `6`; index avg `-0.0` n `26`; metal avg `-0.0149` n `20`; unknown avg `7.1902` n `935`
- 24h: commodity avg `0.8494` n `12`; crypto_alt avg `0.2126` n `234`; crypto_major avg `-0.8189` n `8`; equity avg `-1.2442` n `141`; fx avg `0.0227` n `6`; index avg `-0.2238` n `26`; metal avg `-0.2362` n `20`; unknown avg `2.0473` n `811`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
