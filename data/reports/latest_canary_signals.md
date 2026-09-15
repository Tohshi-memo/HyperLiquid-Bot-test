# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T01:37:31.793190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `-0.1179` n `233`; crypto_major avg `-0.1077` n `8`; equity avg `-0.1885` n `136`; fx avg `-0.0024` n `6`; index avg `-0.0399` n `27`; metal avg `-0.0562` n `20`; unknown avg `0.5416` n `908`
- 1h: commodity avg `-0.0563` n `12`; crypto_alt avg `-0.1773` n `233`; crypto_major avg `-0.0703` n `8`; equity avg `-0.0899` n `136`; fx avg `0.0001` n `6`; index avg `-0.0078` n `27`; metal avg `0.1031` n `20`; unknown avg `0.0462` n `906`
- 4h: commodity avg `0.0598` n `12`; crypto_alt avg `-0.5209` n `233`; crypto_major avg `-0.8486` n `8`; equity avg `0.184` n `136`; fx avg `0.0233` n `6`; index avg `0.0815` n `27`; metal avg `-0.0446` n `20`; unknown avg `0.5335` n `888`
- 24h: commodity avg `-0.1277` n `12`; crypto_alt avg `1.0437` n `233`; crypto_major avg `2.1385` n `8`; equity avg `0.3477` n `136`; fx avg `0.05` n `6`; index avg `0.0359` n `27`; metal avg `-0.3854` n `20`; unknown avg `5.6758` n `794`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
