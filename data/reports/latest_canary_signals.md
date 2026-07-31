# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T05:22:26.666206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0271` n `12`; crypto_alt avg `0.0722` n `230`; crypto_major avg `0.014` n `8`; equity avg `0.1223` n `102`; fx avg `-0.0157` n `6`; index avg `0.0692` n `25`; metal avg `-0.0272` n `20`; unknown avg `-0.1803` n `779`
- 1h: commodity avg `-0.083` n `12`; crypto_alt avg `0.2193` n `230`; crypto_major avg `0.3387` n `8`; equity avg `0.5875` n `102`; fx avg `-0.0511` n `6`; index avg `0.1596` n `25`; metal avg `0.0563` n `20`; unknown avg `5.2621` n `779`
- 4h: commodity avg `-0.1706` n `12`; crypto_alt avg `-0.7371` n `230`; crypto_major avg `-0.7198` n `8`; equity avg `0.0051` n `102`; fx avg `-0.0151` n `6`; index avg `-0.0136` n `25`; metal avg `0.014` n `20`; unknown avg `0.1585` n `779`
- 24h: commodity avg `-0.496` n `12`; crypto_alt avg `0.3115` n `230`; crypto_major avg `1.227` n `8`; equity avg `9.3866` n `102`; fx avg `-0.1148` n `6`; index avg `1.3306` n `25`; metal avg `0.6755` n `20`; unknown avg `0.1093` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
