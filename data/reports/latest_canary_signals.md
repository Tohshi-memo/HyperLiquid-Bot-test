# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T07:52:34.671615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0552` n `12`; crypto_alt avg `-0.3752` n `233`; crypto_major avg `-0.2563` n `8`; equity avg `-0.1465` n `136`; fx avg `0.0021` n `6`; index avg `-0.0302` n `27`; metal avg `-0.1094` n `20`; unknown avg `17.6088` n `908`
- 1h: commodity avg `0.0978` n `12`; crypto_alt avg `-0.4428` n `233`; crypto_major avg `-0.3294` n `8`; equity avg `-0.1066` n `136`; fx avg `0.0151` n `6`; index avg `-0.0535` n `27`; metal avg `-0.1726` n `20`; unknown avg `19.4145` n `904`
- 4h: commodity avg `0.1834` n `12`; crypto_alt avg `-0.9656` n `233`; crypto_major avg `-0.9876` n `8`; equity avg `-0.6382` n `136`; fx avg `0.0838` n `6`; index avg `-0.165` n `27`; metal avg `-0.2729` n `20`; unknown avg `19.9385` n `874`
- 24h: commodity avg `0.0383` n `12`; crypto_alt avg `-1.7156` n `233`; crypto_major avg `-1.0796` n `8`; equity avg `-0.2659` n `136`; fx avg `0.1924` n `6`; index avg `-0.0775` n `27`; metal avg `-0.3526` n `20`; unknown avg `4.4737` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
