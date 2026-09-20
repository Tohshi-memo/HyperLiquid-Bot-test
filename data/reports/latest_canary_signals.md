# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T23:07:29.897620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `-0.1962` n `234`; crypto_major avg `-0.1317` n `8`; equity avg `0.0761` n `140`; fx avg `0.0004` n `6`; index avg `0.0261` n `26`; metal avg `-0.0005` n `20`; unknown avg `5.2879` n `941`
- 1h: commodity avg `-0.1297` n `12`; crypto_alt avg `-0.2996` n `234`; crypto_major avg `0.1646` n `8`; equity avg `0.2524` n `140`; fx avg `0.0317` n `6`; index avg `0.0778` n `26`; metal avg `-0.0056` n `20`; unknown avg `2.0994` n `925`
- 4h: commodity avg `-0.347` n `12`; crypto_alt avg `0.5666` n `234`; crypto_major avg `0.3781` n `8`; equity avg `0.4626` n `140`; fx avg `0.0621` n `6`; index avg `0.1038` n `26`; metal avg `0.0628` n `20`; unknown avg `1.9277` n `853`
- 24h: commodity avg `-0.0139` n `12`; crypto_alt avg `0.7656` n `234`; crypto_major avg `0.2902` n `8`; equity avg `0.3016` n `140`; fx avg `0.0451` n `6`; index avg `0.0556` n `26`; metal avg `0.0194` n `20`; unknown avg `3.2862` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1623`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
