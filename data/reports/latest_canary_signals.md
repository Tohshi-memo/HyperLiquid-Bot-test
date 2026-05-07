# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T03:07:21.814268+00:00`
- Correlation status: `ready`
- Asset price records: `512`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1042` n `12`; crypto_alt avg `0.0369` n `228`; crypto_major avg `-0.0684` n `8`; equity avg `0.0675` n `65`; fx avg `0.0162` n `4`; index avg `0.0046` n `23`; metal avg `0.039` n `18`; unknown avg `0.0038` n `358`
- 1h: commodity avg `0.2168` n `12`; crypto_alt avg `0.1604` n `228`; crypto_major avg `-0.0897` n `8`; equity avg `-0.0075` n `65`; fx avg `0.034` n `4`; index avg `0.0213` n `23`; metal avg `-0.2301` n `18`; unknown avg `-0.1847` n `358`
- 4h: commodity avg `-0.0782` n `12`; crypto_alt avg `-0.4265` n `228`; crypto_major avg `-0.6482` n `8`; equity avg `0.0515` n `65`; fx avg `0.1064` n `4`; index avg `0.1569` n `23`; metal avg `0.247` n `18`; unknown avg `-0.4479` n `356`
- 24h: commodity avg `-1.733` n `7`; crypto_alt avg `0.138` n `223`; crypto_major avg `-1.1742` n `7`; equity avg `1.5325` n `47`; fx avg `-0.2382` n `4`; index avg `1.3072` n `6`; metal avg `1.8777` n `7`; unknown avg `2.0421` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1289`, n `508`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1154`, n `508`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `508`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `508`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0748`, n `504`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0689`, n `504`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0685`, n `504`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `508`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `504`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0629`, n `504`, weak_sample_signal
