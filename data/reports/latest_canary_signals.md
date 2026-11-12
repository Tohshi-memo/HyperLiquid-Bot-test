# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T02:52:25.970744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0273` n `13`; crypto_alt avg `-0.0564` n `239`; crypto_major avg `-0.0268` n `8`; equity avg `-0.2887` n `161`; fx avg `-0.0454` n `6`; index avg `-0.0229` n `27`; metal avg `-0.0031` n `20`; unknown avg `0.8414` n `1262`
- 1h: commodity avg `0.108` n `13`; crypto_alt avg `0.3827` n `239`; crypto_major avg `0.3811` n `8`; equity avg `-0.0062` n `161`; fx avg `-0.0735` n `6`; index avg `0.0191` n `27`; metal avg `-0.0014` n `20`; unknown avg `2.6226` n `1256`
- 4h: commodity avg `-0.0053` n `13`; crypto_alt avg `0.0361` n `239`; crypto_major avg `0.0596` n `8`; equity avg `0.0619` n `161`; fx avg `-0.0995` n `6`; index avg `0.0417` n `27`; metal avg `-0.0302` n `20`; unknown avg `26.2736` n `1250`
- 24h: commodity avg `0.136` n `13`; crypto_alt avg `-1.4563` n `239`; crypto_major avg `-0.1331` n `8`; equity avg `1.5306` n `161`; fx avg `-0.185` n `6`; index avg `0.1702` n `27`; metal avg `-0.3601` n `20`; unknown avg `4.3028` n `1141`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
