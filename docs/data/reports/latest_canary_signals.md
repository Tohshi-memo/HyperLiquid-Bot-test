# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T02:22:27.464559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0224` n `13`; crypto_alt avg `-0.0054` n `235`; crypto_major avg `-0.0084` n `8`; equity avg `-0.0151` n `150`; fx avg `-0.0003` n `6`; index avg `-0.0036` n `26`; metal avg `0.0013` n `20`; unknown avg `0.3316` n `1116`
- 1h: commodity avg `-0.0525` n `13`; crypto_alt avg `0.466` n `235`; crypto_major avg `0.2279` n `8`; equity avg `-0.0086` n `150`; fx avg `-0.0025` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0102` n `20`; unknown avg `-0.0654` n `1114`
- 4h: commodity avg `0.0662` n `13`; crypto_alt avg `1.501` n `235`; crypto_major avg `0.5405` n `8`; equity avg `0.0663` n `150`; fx avg `0.0048` n `6`; index avg `0.041` n `26`; metal avg `0.0198` n `20`; unknown avg `0.2019` n `1108`
- 24h: commodity avg `-0.0893` n `13`; crypto_alt avg `2.7171` n `235`; crypto_major avg `0.689` n `8`; equity avg `0.4949` n `150`; fx avg `-0.0233` n `6`; index avg `0.086` n `26`; metal avg `0.1859` n `20`; unknown avg `13.0645` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
