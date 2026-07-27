# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T22:07:35.742692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0438` n `12`; crypto_alt avg `-0.2419` n `230`; crypto_major avg `-0.2306` n `8`; equity avg `-0.1418` n `102`; fx avg `0.0044` n `6`; index avg `-0.0177` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.0904` n `774`
- 1h: commodity avg `0.0072` n `12`; crypto_alt avg `-0.4821` n `230`; crypto_major avg `-0.5562` n `8`; equity avg `-0.1248` n `102`; fx avg `0.0055` n `6`; index avg `-0.0067` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.1639` n `774`
- 4h: commodity avg `-0.0658` n `12`; crypto_alt avg `-0.2853` n `230`; crypto_major avg `-0.493` n `8`; equity avg `0.5833` n `102`; fx avg `-0.0099` n `6`; index avg `0.1029` n `25`; metal avg `0.0136` n `20`; unknown avg `95.5997` n `774`
- 24h: commodity avg `-0.6066` n `12`; crypto_alt avg `-1.8898` n `230`; crypto_major avg `-1.3806` n `8`; equity avg `-1.4072` n `102`; fx avg `-0.0438` n `6`; index avg `-0.4386` n `25`; metal avg `-0.0072` n `20`; unknown avg `97.454` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1938`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
