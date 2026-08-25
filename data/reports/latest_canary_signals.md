# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T04:51:17.692094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0237` n `12`; crypto_alt avg `0.0444` n `231`; crypto_major avg `0.0136` n `8`; equity avg `0.0033` n `122`; fx avg `-0.0185` n `6`; index avg `-0.0002` n `25`; metal avg `-0.0238` n `20`; unknown avg `0.6387` n `794`
- 1h: commodity avg `-0.0844` n `12`; crypto_alt avg `0.1361` n `231`; crypto_major avg `-0.0442` n `8`; equity avg `0.2515` n `122`; fx avg `-0.0323` n `6`; index avg `0.0491` n `25`; metal avg `-0.0739` n `20`; unknown avg `2.3369` n `794`
- 4h: commodity avg `0.027` n `12`; crypto_alt avg `0.5085` n `231`; crypto_major avg `0.5393` n `8`; equity avg `0.7725` n `122`; fx avg `-0.0168` n `6`; index avg `0.1299` n `25`; metal avg `-0.4923` n `20`; unknown avg `0.3793` n `794`
- 24h: commodity avg `-0.0478` n `12`; crypto_alt avg `1.9746` n `231`; crypto_major avg `2.8935` n `8`; equity avg `-0.4092` n `122`; fx avg `0.0148` n `6`; index avg `-0.0851` n `25`; metal avg `-0.2153` n `20`; unknown avg `0.5937` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
