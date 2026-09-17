# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T03:22:25.400618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `-0.0553` n `234`; crypto_major avg `-0.0468` n `8`; equity avg `-0.0342` n `137`; fx avg `0.0103` n `6`; index avg `-0.0062` n `27`; metal avg `0.0013` n `20`; unknown avg `0.5908` n `921`
- 1h: commodity avg `0.03` n `12`; crypto_alt avg `0.539` n `234`; crypto_major avg `0.518` n `8`; equity avg `0.2531` n `137`; fx avg `-0.0207` n `6`; index avg `0.0239` n `27`; metal avg `0.0447` n `20`; unknown avg `0.777` n `918`
- 4h: commodity avg `0.0752` n `12`; crypto_alt avg `0.9598` n `234`; crypto_major avg `0.6106` n `8`; equity avg `0.2767` n `137`; fx avg `0.0096` n `6`; index avg `0.0604` n `27`; metal avg `0.1923` n `20`; unknown avg `0.9321` n `909`
- 24h: commodity avg `-0.3365` n `12`; crypto_alt avg `1.7644` n `234`; crypto_major avg `1.0267` n `8`; equity avg `1.0398` n `137`; fx avg `-0.0009` n `6`; index avg `0.0609` n `27`; metal avg `-0.3439` n `20`; unknown avg `1.1903` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
