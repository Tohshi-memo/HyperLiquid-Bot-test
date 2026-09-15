# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T12:22:30.582820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1023` n `12`; crypto_alt avg `0.2982` n `233`; crypto_major avg `0.1487` n `8`; equity avg `-0.0139` n `136`; fx avg `0.0079` n `6`; index avg `0.0058` n `27`; metal avg `-0.0526` n `20`; unknown avg `1.4287` n `908`
- 1h: commodity avg `0.1188` n `12`; crypto_alt avg `0.3043` n `233`; crypto_major avg `0.156` n `8`; equity avg `-0.099` n `136`; fx avg `0.0152` n `6`; index avg `0.0049` n `27`; metal avg `-0.0883` n `20`; unknown avg `0.5085` n `906`
- 4h: commodity avg `-0.0851` n `12`; crypto_alt avg `0.3366` n `233`; crypto_major avg `0.4621` n `8`; equity avg `0.6021` n `136`; fx avg `-0.0025` n `6`; index avg `0.145` n `27`; metal avg `0.136` n `20`; unknown avg `1.9884` n `898`
- 24h: commodity avg `-0.0627` n `12`; crypto_alt avg `-1.236` n `233`; crypto_major avg `-0.8162` n `8`; equity avg `0.7119` n `136`; fx avg `0.2053` n `6`; index avg `0.0957` n `27`; metal avg `-0.0377` n `20`; unknown avg `-0.0935` n `818`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
