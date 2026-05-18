# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T15:22:21.105205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0533` n `12`; crypto_alt avg `0.1182` n `228`; crypto_major avg `-0.004` n `8`; equity avg `-0.2515` n `66`; fx avg `-0.0055` n `5`; index avg `-0.1194` n `23`; metal avg `0.1297` n `18`; unknown avg `-0.4752` n `384`
- 1h: commodity avg `0.5736` n `12`; crypto_alt avg `-0.5924` n `228`; crypto_major avg `-0.8729` n `8`; equity avg `-1.0243` n `66`; fx avg `-0.0074` n `5`; index avg `-0.4572` n `23`; metal avg `-0.2506` n `18`; unknown avg `-0.4637` n `384`
- 4h: commodity avg `0.0411` n `12`; crypto_alt avg `-0.1594` n `228`; crypto_major avg `-0.6569` n `8`; equity avg `-1.1778` n `66`; fx avg `-0.0389` n `5`; index avg `-0.2433` n `23`; metal avg `0.4127` n `18`; unknown avg `0.1538` n `383`
- 24h: commodity avg `0.874` n `12`; crypto_alt avg `-2.9426` n `228`; crypto_major avg `-2.4373` n `8`; equity avg `-0.8891` n `66`; fx avg `0.0502` n `5`; index avg `-0.4059` n `23`; metal avg `0.2739` n `18`; unknown avg `-0.527` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
