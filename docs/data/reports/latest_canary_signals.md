# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T07:22:23.597231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0326` n `12`; crypto_alt avg `0.008` n `231`; crypto_major avg `-0.0391` n `8`; equity avg `-0.064` n `122`; fx avg `0.004` n `6`; index avg `-0.0327` n `25`; metal avg `0.0479` n `20`; unknown avg `-0.051` n `794`
- 1h: commodity avg `0.0321` n `12`; crypto_alt avg `-0.4029` n `231`; crypto_major avg `-0.2329` n `8`; equity avg `-0.086` n `122`; fx avg `0.0222` n `6`; index avg `-0.0212` n `25`; metal avg `-0.0019` n `20`; unknown avg `-0.1307` n `794`
- 4h: commodity avg `-0.2226` n `12`; crypto_alt avg `-0.3208` n `231`; crypto_major avg `-0.261` n `8`; equity avg `0.8017` n `122`; fx avg `0.0334` n `6`; index avg `0.1064` n `25`; metal avg `0.1065` n `20`; unknown avg `-0.1908` n `778`
- 24h: commodity avg `-0.1861` n `12`; crypto_alt avg `1.5008` n `231`; crypto_major avg `2.2636` n `8`; equity avg `0.2284` n `122`; fx avg `0.0203` n `6`; index avg `0.0253` n `25`; metal avg `-0.1708` n `20`; unknown avg `0.4793` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
