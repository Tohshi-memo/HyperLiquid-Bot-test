# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T10:52:28.259978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.051` n `13`; crypto_alt avg `-0.1364` n `239`; crypto_major avg `-0.258` n `8`; equity avg `-0.2221` n `165`; fx avg `-0.0039` n `6`; index avg `-0.0308` n `27`; metal avg `-0.0074` n `20`; unknown avg `189.3956` n `1262`
- 1h: commodity avg `0.1282` n `13`; crypto_alt avg `0.0833` n `239`; crypto_major avg `0.3569` n `8`; equity avg `0.6232` n `165`; fx avg `-0.011` n `6`; index avg `0.066` n `27`; metal avg `0.23` n `20`; unknown avg `32.6691` n `1254`
- 4h: commodity avg `-0.3561` n `13`; crypto_alt avg `-0.1551` n `239`; crypto_major avg `-0.2785` n `8`; equity avg `-0.2279` n `165`; fx avg `-0.0357` n `6`; index avg `0.0191` n `27`; metal avg `0.266` n `20`; unknown avg `39.125` n `1194`
- 24h: commodity avg `-0.5131` n `13`; crypto_alt avg `-3.2824` n `239`; crypto_major avg `-2.7949` n `8`; equity avg `-7.6534` n `165`; fx avg `-0.1201` n `6`; index avg `-0.7679` n `27`; metal avg `-1.2499` n `20`; unknown avg `51.0333` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
