# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T16:52:27.413890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0077` n `13`; crypto_alt avg `0.0179` n `239`; crypto_major avg `0.178` n `8`; equity avg `0.0625` n `168`; fx avg `-0.0106` n `6`; index avg `0.0027` n `27`; metal avg `0.0148` n `20`; unknown avg `2.9695` n `1259`
- 1h: commodity avg `-0.018` n `13`; crypto_alt avg `-0.3491` n `239`; crypto_major avg `-0.1486` n `8`; equity avg `-0.0377` n `168`; fx avg `-0.0` n `6`; index avg `-0.0008` n `27`; metal avg `0.0083` n `20`; unknown avg `0.3215` n `1239`
- 4h: commodity avg `-0.0242` n `13`; crypto_alt avg `-0.9417` n `239`; crypto_major avg `-0.0022` n `8`; equity avg `-0.1334` n `168`; fx avg `0.0217` n `6`; index avg `-0.0066` n `27`; metal avg `-0.0252` n `20`; unknown avg `1.7379` n `1235`
- 24h: commodity avg `-0.067` n `13`; crypto_alt avg `-3.2147` n `239`; crypto_major avg `-1.5984` n `8`; equity avg `0.0161` n `168`; fx avg `-0.0134` n `6`; index avg `-0.0002` n `27`; metal avg `0.2354` n `20`; unknown avg `192.4795` n `1078`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
