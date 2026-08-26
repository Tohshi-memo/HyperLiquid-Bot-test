# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T08:52:51.439689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.0744` n `231`; crypto_major avg `-0.1194` n `8`; equity avg `0.0089` n `122`; fx avg `-0.0016` n `6`; index avg `0.0039` n `25`; metal avg `-0.0205` n `20`; unknown avg `0.0548` n `797`
- 1h: commodity avg `-0.0478` n `12`; crypto_alt avg `0.0203` n `231`; crypto_major avg `-0.237` n `8`; equity avg `0.1187` n `122`; fx avg `-0.0065` n `6`; index avg `0.0201` n `25`; metal avg `-0.047` n `20`; unknown avg `0.0562` n `797`
- 4h: commodity avg `-0.1495` n `12`; crypto_alt avg `0.1786` n `231`; crypto_major avg `0.0199` n `8`; equity avg `-0.2871` n `122`; fx avg `-0.0152` n `6`; index avg `-0.0399` n `25`; metal avg `-0.1106` n `20`; unknown avg `0.0702` n `781`
- 24h: commodity avg `-0.5406` n `12`; crypto_alt avg `-1.5743` n `231`; crypto_major avg `-1.7111` n `8`; equity avg `0.5211` n `122`; fx avg `-0.0517` n `6`; index avg `0.0433` n `25`; metal avg `0.234` n `20`; unknown avg `0.9519` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
