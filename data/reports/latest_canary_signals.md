# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T09:52:28.177683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `13`; crypto_alt avg `-0.0874` n `238`; crypto_major avg `-0.0935` n `8`; equity avg `-0.0026` n `156`; fx avg `-0.006` n `6`; index avg `0.0041` n `27`; metal avg `0.0067` n `20`; unknown avg `-0.1513` n `1262`
- 1h: commodity avg `-0.0481` n `13`; crypto_alt avg `0.0365` n `238`; crypto_major avg `0.0915` n `8`; equity avg `0.0562` n `156`; fx avg `-0.0137` n `6`; index avg `0.0009` n `27`; metal avg `0.0274` n `20`; unknown avg `-0.1052` n `1256`
- 4h: commodity avg `-0.0108` n `13`; crypto_alt avg `0.0446` n `238`; crypto_major avg `-0.2478` n `8`; equity avg `-0.0138` n `156`; fx avg `0.0015` n `6`; index avg `-0.0004` n `27`; metal avg `0.0178` n `20`; unknown avg `0.6645` n `1212`
- 24h: commodity avg `-0.2692` n `13`; crypto_alt avg `0.8105` n `238`; crypto_major avg `-0.7655` n `8`; equity avg `-1.6497` n `156`; fx avg `-0.1041` n `6`; index avg `-0.1658` n `27`; metal avg `-0.4502` n `20`; unknown avg `4.3808` n `1043`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
