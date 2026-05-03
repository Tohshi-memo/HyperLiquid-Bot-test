# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T05:30:24.630674+00:00`
- Correlation status: `ready`
- Asset price records: `141`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `7`; crypto_alt avg `-0.061` n `223`; crypto_major avg `0.0129` n `7`; equity avg `0.0415` n `42`; fx avg `0.0021` n `4`; index avg `0.012` n `9`; metal avg `0.0076` n `7`; unknown avg `0.0165` n `313`
- 1h: commodity avg `-0.0013` n `7`; crypto_alt avg `0.0911` n `223`; crypto_major avg `0.0349` n `7`; equity avg `-0.0801` n `42`; fx avg `-0.0005` n `4`; index avg `0.0123` n `9`; metal avg `0.0071` n `7`; unknown avg `0.3235` n `313`
- 4h: commodity avg `0.0207` n `7`; crypto_alt avg `-0.297` n `223`; crypto_major avg `-0.0498` n `7`; equity avg `-0.1384` n `42`; fx avg `0.0011` n `4`; index avg `-0.076` n `9`; metal avg `0.0432` n `7`; unknown avg `0.2284` n `313`
- 24h: commodity avg `-0.1125` n `7`; crypto_alt avg `1.3721` n `223`; crypto_major avg `0.0339` n `7`; equity avg `0.5715` n `42`; fx avg `0.1127` n `4`; index avg `0.0046` n `9`; metal avg `0.0892` n `7`; unknown avg `0.36` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.443`, n `137`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4278`, n `137`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4085`, n `133`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4064`, n `133`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4043`, n `137`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.397`, n `133`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3922`, n `133`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3864`, n `137`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3619`, n `133`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3547`, n `137`, moderate_sample_signal
