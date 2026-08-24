# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T22:07:24.520450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `0.0319` n `231`; crypto_major avg `0.086` n `8`; equity avg `0.0088` n `122`; fx avg `-0.0019` n `6`; index avg `0.0056` n `25`; metal avg `0.0315` n `20`; unknown avg `-0.1773` n `794`
- 1h: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.0208` n `231`; crypto_major avg `0.142` n `8`; equity avg `0.0258` n `122`; fx avg `0.0036` n `6`; index avg `0.0054` n `25`; metal avg `0.0466` n `20`; unknown avg `-0.2204` n `794`
- 4h: commodity avg `-0.0242` n `12`; crypto_alt avg `0.1606` n `231`; crypto_major avg `0.4234` n `8`; equity avg `-0.2842` n `122`; fx avg `-0.0016` n `6`; index avg `-0.0242` n `25`; metal avg `0.1377` n `20`; unknown avg `-0.5769` n `794`
- 24h: commodity avg `-0.1993` n `12`; crypto_alt avg `-1.4273` n `231`; crypto_major avg `-0.7326` n `8`; equity avg `-2.71` n `122`; fx avg `-0.0569` n `6`; index avg `-0.3139` n `25`; metal avg `0.1861` n `20`; unknown avg `0.7426` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
