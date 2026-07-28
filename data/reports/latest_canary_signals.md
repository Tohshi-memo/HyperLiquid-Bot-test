# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T16:48:11.228634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.25` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.7874` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.149` n `12`; crypto_alt avg `0.0498` n `230`; crypto_major avg `0.2106` n `8`; equity avg `0.1602` n `102`; fx avg `0.0119` n `6`; index avg `0.001` n `25`; metal avg `-0.0473` n `20`; unknown avg `-0.0192` n `774`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `-0.0154` n `230`; crypto_major avg `0.2001` n `8`; equity avg `-0.0132` n `102`; fx avg `0.0117` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0484` n `20`; unknown avg `-0.1385` n `774`
- 4h: commodity avg `-0.61` n `12`; crypto_alt avg `0.4184` n `230`; crypto_major avg `1.1178` n `8`; equity avg `-0.6696` n `102`; fx avg `0.0005` n `6`; index avg `0.0874` n `25`; metal avg `0.0783` n `20`; unknown avg `-0.2155` n `774`
- 24h: commodity avg `-1.1853` n `12`; crypto_alt avg `-1.738` n `230`; crypto_major avg `-1.4926` n `8`; equity avg `-2.6278` n `102`; fx avg `-0.0834` n `6`; index avg `-0.1592` n `25`; metal avg `-0.3507` n `20`; unknown avg `1225.4188` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
