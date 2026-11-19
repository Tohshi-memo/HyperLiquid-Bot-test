# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T00:52:26.418704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `13`; crypto_alt avg `0.0707` n `239`; crypto_major avg `0.0579` n `8`; equity avg `0.2464` n `164`; fx avg `0.0292` n `6`; index avg `0.0501` n `27`; metal avg `0.0485` n `20`; unknown avg `0.3138` n `1265`
- 1h: commodity avg `-0.0299` n `13`; crypto_alt avg `0.0306` n `239`; crypto_major avg `-0.0732` n `8`; equity avg `0.535` n `164`; fx avg `-0.0154` n `6`; index avg `0.081` n `27`; metal avg `0.1536` n `20`; unknown avg `0.1196` n `1257`
- 4h: commodity avg `-0.1047` n `13`; crypto_alt avg `0.7835` n `239`; crypto_major avg `0.7527` n `8`; equity avg `1.3564` n `164`; fx avg `-0.0186` n `6`; index avg `0.1889` n `27`; metal avg `0.2732` n `20`; unknown avg `1.3186` n `1221`
- 24h: commodity avg `-0.2259` n `13`; crypto_alt avg `-0.6174` n `239`; crypto_major avg `-1.7861` n `8`; equity avg `-1.4518` n `164`; fx avg `-0.1073` n `6`; index avg `-0.0442` n `27`; metal avg `-0.6523` n `20`; unknown avg `77.4154` n `1127`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
