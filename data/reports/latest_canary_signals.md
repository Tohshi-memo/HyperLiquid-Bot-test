# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T10:37:30.262836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `0.3398` n `231`; crypto_major avg `0.4666` n `8`; equity avg `0.0759` n `122`; fx avg `-0.0069` n `6`; index avg `0.0222` n `25`; metal avg `0.0225` n `20`; unknown avg `-0.014` n `797`
- 1h: commodity avg `0.0388` n `12`; crypto_alt avg `0.5387` n `231`; crypto_major avg `0.7624` n `8`; equity avg `0.1268` n `122`; fx avg `-0.0142` n `6`; index avg `0.0044` n `25`; metal avg `0.0166` n `20`; unknown avg `0.1401` n `797`
- 4h: commodity avg `-0.0958` n `12`; crypto_alt avg `0.1037` n `231`; crypto_major avg `0.3763` n `8`; equity avg `0.0029` n `122`; fx avg `-0.0256` n `6`; index avg `-0.0312` n `25`; metal avg `-0.031` n `20`; unknown avg `-0.0218` n `797`
- 24h: commodity avg `-0.2492` n `12`; crypto_alt avg `-1.3962` n `231`; crypto_major avg `-1.0406` n `8`; equity avg `0.1511` n `122`; fx avg `-0.0383` n `6`; index avg `-0.0462` n `25`; metal avg `0.1706` n `20`; unknown avg `0.7217` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
