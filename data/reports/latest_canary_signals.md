# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T17:22:30.186512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0649` n `12`; crypto_alt avg `-0.1264` n `234`; crypto_major avg `-0.083` n `8`; equity avg `-0.0047` n `141`; fx avg `0.0027` n `6`; index avg `0.0042` n `26`; metal avg `-0.0086` n `20`; unknown avg `0.205` n `960`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `0.0722` n `234`; crypto_major avg `-0.0837` n `8`; equity avg `0.0278` n `141`; fx avg `0.0268` n `6`; index avg `0.0123` n `26`; metal avg `0.0018` n `20`; unknown avg `3.7641` n `958`
- 4h: commodity avg `-0.2279` n `12`; crypto_alt avg `-0.1758` n `234`; crypto_major avg `-0.6126` n `8`; equity avg `-0.5321` n `141`; fx avg `0.012` n `6`; index avg `0.0479` n `26`; metal avg `0.1024` n `20`; unknown avg `9.3755` n `894`
- 24h: commodity avg `-0.9751` n `12`; crypto_alt avg `1.5869` n `234`; crypto_major avg `0.4584` n `8`; equity avg `0.1802` n `141`; fx avg `-0.2343` n `6`; index avg `0.1854` n `26`; metal avg `0.2153` n `20`; unknown avg `1601.3446` n `805`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
