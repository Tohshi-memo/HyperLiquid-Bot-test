# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T12:07:26.089416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0557` n `13`; crypto_alt avg `-0.0224` n `239`; crypto_major avg `0.0715` n `8`; equity avg `0.1032` n `158`; fx avg `0.0182` n `6`; index avg `0.0064` n `27`; metal avg `-0.0368` n `20`; unknown avg `0.0518` n `1233`
- 1h: commodity avg `0.0353` n `13`; crypto_alt avg `0.307` n `239`; crypto_major avg `0.4272` n `8`; equity avg `1.009` n `158`; fx avg `0.0502` n `6`; index avg `0.0776` n `27`; metal avg `0.0895` n `20`; unknown avg `31.6461` n `1193`
- 4h: commodity avg `-0.0758` n `13`; crypto_alt avg `0.9024` n `239`; crypto_major avg `0.9404` n `8`; equity avg `2.0727` n `158`; fx avg `0.0585` n `6`; index avg `0.2331` n `27`; metal avg `0.1069` n `20`; unknown avg `29.2207` n `1168`
- 24h: commodity avg `0.6735` n `13`; crypto_alt avg `-2.5509` n `239`; crypto_major avg `-4.741` n `8`; equity avg `-3.7675` n `158`; fx avg `0.0083` n `6`; index avg `-0.5763` n `27`; metal avg `-0.3642` n `20`; unknown avg `14.5825` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
