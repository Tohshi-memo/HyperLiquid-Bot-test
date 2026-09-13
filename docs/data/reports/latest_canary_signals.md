# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T16:37:27.177677+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.0172` n `233`; crypto_major avg `-0.0403` n `8`; equity avg `-0.0104` n `136`; fx avg `0.0006` n `6`; index avg `-0.0013` n `27`; metal avg `0.0038` n `20`; unknown avg `0.0803` n `832`
- 1h: commodity avg `-0.0136` n `12`; crypto_alt avg `0.1477` n `233`; crypto_major avg `0.247` n `8`; equity avg `0.1829` n `136`; fx avg `-0.0033` n `6`; index avg `0.0348` n `27`; metal avg `0.0073` n `20`; unknown avg `0.5433` n `830`
- 4h: commodity avg `-0.0132` n `12`; crypto_alt avg `0.0754` n `233`; crypto_major avg `0.692` n `8`; equity avg `0.3716` n `136`; fx avg `0.0078` n `6`; index avg `0.0693` n `27`; metal avg `0.0103` n `20`; unknown avg `1.3486` n `830`
- 24h: commodity avg `0.2732` n `12`; crypto_alt avg `-0.645` n `233`; crypto_major avg `-1.2307` n `8`; equity avg `-1.5768` n `136`; fx avg `0.0106` n `6`; index avg `-0.2606` n `26`; metal avg `-0.0888` n `20`; unknown avg `-0.1869` n `708`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
