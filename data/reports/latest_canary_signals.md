# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T01:37:36.883452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `13`; crypto_alt avg `-0.276` n `239`; crypto_major avg `-0.1943` n `8`; equity avg `-0.1585` n `165`; fx avg `-0.0152` n `6`; index avg `-0.0232` n `27`; metal avg `-0.0151` n `20`; unknown avg `3.3202` n `1262`
- 1h: commodity avg `-0.0326` n `13`; crypto_alt avg `-0.3268` n `239`; crypto_major avg `-0.0255` n `8`; equity avg `-0.1739` n `165`; fx avg `-0.0632` n `6`; index avg `0.0168` n `27`; metal avg `-0.2375` n `20`; unknown avg `3.9614` n `1254`
- 4h: commodity avg `-0.0782` n `13`; crypto_alt avg `0.1026` n `239`; crypto_major avg `0.5459` n `8`; equity avg `-0.6328` n `165`; fx avg `-0.0094` n `6`; index avg `-0.0743` n `27`; metal avg `-0.447` n `20`; unknown avg `1.1036` n `1242`
- 24h: commodity avg `-0.1109` n `13`; crypto_alt avg `-0.9536` n `239`; crypto_major avg `-0.1946` n `8`; equity avg `-4.6173` n `165`; fx avg `-0.0048` n `6`; index avg `-0.3278` n `27`; metal avg `-1.4378` n `20`; unknown avg `6.9433` n `1168`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
