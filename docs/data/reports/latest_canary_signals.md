# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T17:07:29.069363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `12`; crypto_alt avg `0.2391` n `233`; crypto_major avg `0.135` n `8`; equity avg `0.0189` n `136`; fx avg `0.0027` n `6`; index avg `-0.0074` n `27`; metal avg `0.0099` n `20`; unknown avg `1.329` n `816`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `0.3321` n `233`; crypto_major avg `0.3303` n `8`; equity avg `0.1563` n `136`; fx avg `-0.0006` n `6`; index avg `-0.0078` n `27`; metal avg `0.021` n `20`; unknown avg `11.3507` n `810`
- 4h: commodity avg `-0.0176` n `12`; crypto_alt avg `0.6194` n `233`; crypto_major avg `0.925` n `8`; equity avg `0.4492` n `136`; fx avg `0.0099` n `6`; index avg `0.0575` n `27`; metal avg `0.0278` n `20`; unknown avg `4.5454` n `810`
- 24h: commodity avg `0.2764` n `12`; crypto_alt avg `-0.2484` n `233`; crypto_major avg `-1.0123` n `8`; equity avg `-1.5107` n `136`; fx avg `0.0098` n `6`; index avg `-0.2614` n `26`; metal avg `-0.072` n `20`; unknown avg `1.9713` n `706`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
