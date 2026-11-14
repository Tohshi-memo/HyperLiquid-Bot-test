# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T09:37:31.880456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `13`; crypto_alt avg `0.1204` n `239`; crypto_major avg `0.2537` n `8`; equity avg `0.0838` n `162`; fx avg `0.0016` n `6`; index avg `0.0102` n `27`; metal avg `0.0125` n `20`; unknown avg `12.1271` n `1258`
- 1h: commodity avg `-0.0364` n `13`; crypto_alt avg `0.1562` n `239`; crypto_major avg `0.2493` n `8`; equity avg `0.0346` n `162`; fx avg `-0.1765` n `6`; index avg `0.0003` n `27`; metal avg `0.0215` n `20`; unknown avg `12.6323` n `1203`
- 4h: commodity avg `0.0005` n `13`; crypto_alt avg `-0.6908` n `239`; crypto_major avg `0.0955` n `8`; equity avg `0.1373` n `162`; fx avg `-0.0055` n `6`; index avg `0.0026` n `27`; metal avg `0.0438` n `20`; unknown avg `13.0668` n `1170`
- 24h: commodity avg `-0.1844` n `13`; crypto_alt avg `-2.7168` n `239`; crypto_major avg `-3.0933` n `8`; equity avg `-2.7017` n `162`; fx avg `-0.1365` n `6`; index avg `-0.2284` n `27`; metal avg `-0.3808` n `20`; unknown avg `0.7527` n `1042`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
