# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T08:21:34.254341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0769` n `12`; crypto_alt avg `0.1065` n `231`; crypto_major avg `0.0654` n `8`; equity avg `-0.0645` n `122`; fx avg `-0.0085` n `6`; index avg `-0.016` n `25`; metal avg `-0.0084` n `20`; unknown avg `0.008` n `797`
- 1h: commodity avg `0.0409` n `12`; crypto_alt avg `-0.1224` n `231`; crypto_major avg `-0.1553` n `8`; equity avg `-0.0737` n `122`; fx avg `-0.0146` n `6`; index avg `-0.0317` n `25`; metal avg `-0.0446` n `20`; unknown avg `0.0529` n `797`
- 4h: commodity avg `0.068` n `12`; crypto_alt avg `-0.1271` n `231`; crypto_major avg `-0.0771` n `8`; equity avg `-0.4981` n `122`; fx avg `0.001` n `6`; index avg `-0.0782` n `25`; metal avg `-0.1213` n `20`; unknown avg `0.0068` n `781`
- 24h: commodity avg `-0.6022` n `12`; crypto_alt avg `-1.9437` n `231`; crypto_major avg `-2.0436` n `8`; equity avg `0.4886` n `122`; fx avg `-0.0591` n `6`; index avg `0.0496` n `25`; metal avg `0.1862` n `20`; unknown avg `0.898` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
