# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T13:37:28.108162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0254` n `13`; crypto_alt avg `0.0705` n `239`; crypto_major avg `0.0297` n `8`; equity avg `-0.0294` n `168`; fx avg `0.0069` n `6`; index avg `-0.0181` n `27`; metal avg `0.0314` n `20`; unknown avg `4.5538` n `1264`
- 1h: commodity avg `-0.1689` n `13`; crypto_alt avg `0.0098` n `239`; crypto_major avg `0.1047` n `8`; equity avg `0.0538` n `168`; fx avg `-0.0306` n `6`; index avg `0.0075` n `27`; metal avg `-0.2169` n `20`; unknown avg `2.0993` n `1255`
- 4h: commodity avg `-0.4045` n `13`; crypto_alt avg `-0.174` n `239`; crypto_major avg `-0.3834` n `8`; equity avg `-0.7036` n `168`; fx avg `0.0028` n `6`; index avg `-0.0127` n `27`; metal avg `-0.5051` n `20`; unknown avg `186.9073` n `1249`
- 24h: commodity avg `-0.2704` n `13`; crypto_alt avg `1.9041` n `239`; crypto_major avg `2.5882` n `8`; equity avg `3.2289` n `168`; fx avg `-0.1091` n `6`; index avg `0.2633` n `27`; metal avg `0.8479` n `20`; unknown avg `344.5532` n `1027`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
