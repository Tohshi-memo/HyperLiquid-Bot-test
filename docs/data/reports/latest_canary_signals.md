# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T01:52:25.119721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0347` n `12`; crypto_alt avg `0.3051` n `229`; crypto_major avg `0.1637` n `8`; equity avg `0.4485` n `91`; fx avg `-0.0268` n `6`; index avg `0.1033` n `25`; metal avg `0.1106` n `20`; unknown avg `0.1842` n `761`
- 1h: commodity avg `0.0157` n `12`; crypto_alt avg `-0.396` n `229`; crypto_major avg `-0.4186` n `8`; equity avg `-0.1115` n `91`; fx avg `-0.0536` n `6`; index avg `-0.0414` n `25`; metal avg `0.0128` n `20`; unknown avg `-0.1771` n `761`
- 4h: commodity avg `0.0597` n `12`; crypto_alt avg `-0.8475` n `229`; crypto_major avg `-0.8461` n `8`; equity avg `-0.9417` n `91`; fx avg `-0.0797` n `6`; index avg `-0.2671` n `25`; metal avg `-0.1657` n `20`; unknown avg `0.6418` n `761`
- 24h: commodity avg `0.2779` n `12`; crypto_alt avg `0.32` n `229`; crypto_major avg `-0.3092` n `8`; equity avg `-0.6015` n `90`; fx avg `0.0238` n `6`; index avg `-0.0878` n `25`; metal avg `-0.4261` n `20`; unknown avg `-0.3297` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
