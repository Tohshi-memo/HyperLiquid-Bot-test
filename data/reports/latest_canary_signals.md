# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T16:01:09.330144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `0.0012` n `230`; crypto_major avg `-0.0736` n `8`; equity avg `-0.0361` n `92`; fx avg `-0.0009` n `6`; index avg `-0.0173` n `25`; metal avg `0.0123` n `20`; unknown avg `-0.0076` n `766`
- 1h: commodity avg `0.1155` n `12`; crypto_alt avg `-0.4789` n `230`; crypto_major avg `-0.389` n `8`; equity avg `-0.4528` n `92`; fx avg `-0.0054` n `6`; index avg `-0.1072` n `25`; metal avg `-0.0191` n `20`; unknown avg `-0.0917` n `766`
- 4h: commodity avg `0.164` n `12`; crypto_alt avg `-0.2581` n `230`; crypto_major avg `-0.4875` n `8`; equity avg `-0.3393` n `92`; fx avg `-0.031` n `6`; index avg `-0.0156` n `25`; metal avg `-0.1385` n `20`; unknown avg `-0.0691` n `766`
- 24h: commodity avg `0.1472` n `12`; crypto_alt avg `-1.6335` n `230`; crypto_major avg `-2.5219` n `8`; equity avg `-2.4324` n `92`; fx avg `-0.0679` n `6`; index avg `-0.5226` n `25`; metal avg `-0.3944` n `20`; unknown avg `-0.1694` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
