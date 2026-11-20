# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T10:37:26.889450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.043` n `13`; crypto_alt avg `0.3697` n `239`; crypto_major avg `0.6911` n `8`; equity avg `0.5321` n `165`; fx avg `0.0253` n `6`; index avg `0.0659` n `27`; metal avg `0.1626` n `20`; unknown avg `1.6113` n `1262`
- 1h: commodity avg `0.0388` n `13`; crypto_alt avg `0.1785` n `239`; crypto_major avg `0.7576` n `8`; equity avg `0.6694` n `165`; fx avg `0.0005` n `6`; index avg `0.0646` n `27`; metal avg `0.1978` n `20`; unknown avg `191.8718` n `1256`
- 4h: commodity avg `-0.4253` n `13`; crypto_alt avg `0.1016` n `239`; crypto_major avg `0.1897` n `8`; equity avg `-0.0288` n `165`; fx avg `-0.0335` n `6`; index avg `0.0492` n `27`; metal avg `0.3249` n `20`; unknown avg `41.9769` n `1194`
- 24h: commodity avg `-0.6684` n `13`; crypto_alt avg `-3.141` n `239`; crypto_major avg `-2.4393` n `8`; equity avg `-7.3756` n `165`; fx avg `-0.1149` n `6`; index avg `-0.7205` n `27`; metal avg `-1.2128` n `20`; unknown avg `43.0049` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
