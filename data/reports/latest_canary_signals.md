# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T01:07:30.384656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0558` n `13`; crypto_alt avg `0.0481` n `239`; crypto_major avg `0.1401` n `8`; equity avg `0.1073` n `164`; fx avg `0.0047` n `6`; index avg `-0.0147` n `27`; metal avg `0.0047` n `20`; unknown avg `9.7601` n `1259`
- 1h: commodity avg `0.0248` n `13`; crypto_alt avg `0.3515` n `239`; crypto_major avg `0.5289` n `8`; equity avg `0.6112` n `164`; fx avg `0.02` n `6`; index avg `0.0606` n `27`; metal avg `0.1616` n `20`; unknown avg `10.8257` n `1263`
- 4h: commodity avg `0.0079` n `13`; crypto_alt avg `0.6582` n `239`; crypto_major avg `0.7738` n `8`; equity avg `1.5577` n `164`; fx avg `-0.0129` n `6`; index avg `0.1805` n `27`; metal avg `0.3093` n `20`; unknown avg `1.826` n `1247`
- 24h: commodity avg `-0.1283` n `13`; crypto_alt avg `-0.4258` n `239`; crypto_major avg `-1.4536` n `8`; equity avg `-0.8556` n `164`; fx avg `-0.0884` n `6`; index avg `0.0084` n `27`; metal avg `-0.6843` n `20`; unknown avg `107.8504` n `1129`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
