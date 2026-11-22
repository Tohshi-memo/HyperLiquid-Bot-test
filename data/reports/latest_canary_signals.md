# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T14:37:26.205826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `-0.0774` n `239`; crypto_major avg `-0.07` n `8`; equity avg `-0.067` n `166`; fx avg `-0.0062` n `6`; index avg `-0.0043` n `27`; metal avg `-0.0018` n `20`; unknown avg `-0.0076` n `1259`
- 1h: commodity avg `-0.0168` n `13`; crypto_alt avg `-0.1074` n `239`; crypto_major avg `-0.1769` n `8`; equity avg `-0.094` n `166`; fx avg `-0.0142` n `6`; index avg `-0.0079` n `27`; metal avg `-0.0024` n `20`; unknown avg `159.8705` n `1253`
- 4h: commodity avg `-0.0385` n `13`; crypto_alt avg `-0.0871` n `239`; crypto_major avg `-0.2172` n `8`; equity avg `0.0684` n `166`; fx avg `-0.0038` n `6`; index avg `0.0404` n `27`; metal avg `-0.0048` n `20`; unknown avg `160.6739` n `1245`
- 24h: commodity avg `-0.0345` n `13`; crypto_alt avg `0.4514` n `239`; crypto_major avg `0.6069` n `8`; equity avg `1.0002` n `166`; fx avg `-0.0199` n `6`; index avg `0.157` n `27`; metal avg `0.0105` n `20`; unknown avg `-0.1619` n `1078`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
