# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T12:52:25.795861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.68` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `-0.1592` n `239`; crypto_major avg `-0.0758` n `8`; equity avg `-0.027` n `168`; fx avg `-0.025` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0072` n `20`; unknown avg `-0.0842` n `1265`
- 1h: commodity avg `0.0048` n `13`; crypto_alt avg `-0.1425` n `239`; crypto_major avg `0.0007` n `8`; equity avg `-0.0217` n `168`; fx avg `-0.0188` n `6`; index avg `0.0051` n `27`; metal avg `-0.0049` n `20`; unknown avg `7.6592` n `1249`
- 4h: commodity avg `-0.0355` n `13`; crypto_alt avg `-0.5551` n `239`; crypto_major avg `-0.296` n `8`; equity avg `-0.0921` n `168`; fx avg `-0.0172` n `6`; index avg `-0.0104` n `27`; metal avg `0.0196` n `20`; unknown avg `306.579` n `1229`
- 24h: commodity avg `-0.4003` n `13`; crypto_alt avg `-3.5759` n `239`; crypto_major avg `-3.0124` n `8`; equity avg `-0.0896` n `168`; fx avg `-0.1205` n `6`; index avg `0.0172` n `27`; metal avg `-0.0398` n `20`; unknown avg `190.3678` n `1089`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
