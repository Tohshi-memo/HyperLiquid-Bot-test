# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T08:22:29.175137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0588` n `12`; crypto_alt avg `-0.037` n `230`; crypto_major avg `0.1477` n `8`; equity avg `-0.6064` n `108`; fx avg `-0.008` n `6`; index avg `-0.0757` n `25`; metal avg `-0.081` n `20`; unknown avg `0.0143` n `781`
- 1h: commodity avg `0.0332` n `12`; crypto_alt avg `0.1502` n `230`; crypto_major avg `0.415` n `8`; equity avg `-0.6116` n `108`; fx avg `0.0326` n `6`; index avg `-0.0827` n `25`; metal avg `-0.1158` n `20`; unknown avg `0.1296` n `781`
- 4h: commodity avg `0.2454` n `12`; crypto_alt avg `0.2173` n `230`; crypto_major avg `0.5195` n `8`; equity avg `-0.5092` n `108`; fx avg `0.0814` n `6`; index avg `-0.0539` n `25`; metal avg `0.1651` n `20`; unknown avg `0.1405` n `749`
- 24h: commodity avg `-1.1553` n `12`; crypto_alt avg `0.6616` n `230`; crypto_major avg `1.0655` n `8`; equity avg `2.1674` n `108`; fx avg `-0.0079` n `6`; index avg `0.5695` n `25`; metal avg `1.1046` n `20`; unknown avg `0.1479` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
