# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T18:37:23.451648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0565` n `13`; crypto_alt avg `0.1317` n `239`; crypto_major avg `0.0578` n `8`; equity avg `0.267` n `162`; fx avg `0.0024` n `6`; index avg `0.0299` n `27`; metal avg `-0.0236` n `20`; unknown avg `1.1835` n `1262`
- 1h: commodity avg `0.0663` n `13`; crypto_alt avg `0.0361` n `239`; crypto_major avg `0.0495` n `8`; equity avg `0.1943` n `162`; fx avg `-0.0264` n `6`; index avg `0.011` n `27`; metal avg `-0.0314` n `20`; unknown avg `0.3832` n `1260`
- 4h: commodity avg `-0.1999` n `13`; crypto_alt avg `-0.6558` n `239`; crypto_major avg `-0.67` n `8`; equity avg `-0.9888` n `162`; fx avg `-0.0911` n `6`; index avg `-0.1136` n `27`; metal avg `-0.2286` n `20`; unknown avg `-0.4635` n `1250`
- 24h: commodity avg `-0.0709` n `13`; crypto_alt avg `0.1082` n `239`; crypto_major avg `-1.6337` n `8`; equity avg `-3.029` n `162`; fx avg `-0.0509` n `6`; index avg `-0.2636` n `27`; metal avg `-0.2784` n `20`; unknown avg `2.4053` n `1089`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
