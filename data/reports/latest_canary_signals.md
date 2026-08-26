# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T11:52:14.344137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `0.1227` n `231`; crypto_major avg `-0.0094` n `8`; equity avg `-0.0626` n `122`; fx avg `0.0044` n `6`; index avg `-0.0046` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.0221` n `797`
- 1h: commodity avg `0.0734` n `12`; crypto_alt avg `-0.3573` n `231`; crypto_major avg `-0.7303` n `8`; equity avg `-0.1432` n `122`; fx avg `0.0131` n `6`; index avg `0.0055` n `25`; metal avg `-0.0368` n `20`; unknown avg `-0.0711` n `797`
- 4h: commodity avg `0.2009` n `12`; crypto_alt avg `-0.2455` n `231`; crypto_major avg `-0.4056` n `8`; equity avg `0.03` n `122`; fx avg `-0.0032` n `6`; index avg `0.0139` n `25`; metal avg `-0.084` n `20`; unknown avg `-0.068` n `797`
- 24h: commodity avg `-0.1084` n `12`; crypto_alt avg `-1.3562` n `231`; crypto_major avg `-1.1811` n `8`; equity avg `0.1006` n `122`; fx avg `-0.0021` n `6`; index avg `-0.0422` n `25`; metal avg `0.0752` n `20`; unknown avg `0.5936` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
