# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T17:37:29.619468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `-0.1498` n `233`; crypto_major avg `-0.0796` n `8`; equity avg `0.0021` n `136`; fx avg `0.0082` n `6`; index avg `-0.0088` n `27`; metal avg `-0.0029` n `20`; unknown avg `0.4899` n `824`
- 1h: commodity avg `0.0211` n `12`; crypto_alt avg `0.4004` n `233`; crypto_major avg `0.2545` n `8`; equity avg `0.0969` n `136`; fx avg `0.0014` n `6`; index avg `-0.0198` n `27`; metal avg `0.0162` n `20`; unknown avg `5.2385` n `780`
- 4h: commodity avg `-0.019` n `12`; crypto_alt avg `0.6518` n `233`; crypto_major avg `1.0418` n `8`; equity avg `0.545` n `136`; fx avg `0.0088` n `6`; index avg `0.0399` n `27`; metal avg `0.0355` n `20`; unknown avg `4.381` n `774`
- 24h: commodity avg `0.2696` n `12`; crypto_alt avg `-0.194` n `233`; crypto_major avg `-0.9407` n `8`; equity avg `-1.4401` n `136`; fx avg `0.0124` n `6`; index avg `-0.2696` n `26`; metal avg `-0.0677` n `20`; unknown avg `1.8874` n `688`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
