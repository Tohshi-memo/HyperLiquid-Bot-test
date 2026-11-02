# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T01:22:40.431733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `13`; crypto_alt avg `0.3688` n `238`; crypto_major avg `0.4789` n `8`; equity avg `0.2434` n `156`; fx avg `-0.0005` n `6`; index avg `0.0256` n `27`; metal avg `-0.0675` n `20`; unknown avg `0.1435` n `1263`
- 1h: commodity avg `-0.1444` n `13`; crypto_alt avg `0.767` n `238`; crypto_major avg `0.9355` n `8`; equity avg `0.739` n `156`; fx avg `0.0577` n `6`; index avg `0.13` n `27`; metal avg `-0.0059` n `20`; unknown avg `0.379` n `1253`
- 4h: commodity avg `-0.0782` n `13`; crypto_alt avg `0.555` n `238`; crypto_major avg `0.92` n `8`; equity avg `0.8804` n `156`; fx avg `0.1378` n `6`; index avg `0.1981` n `27`; metal avg `0.1108` n `20`; unknown avg `-0.3253` n `1225`
- 24h: commodity avg `-0.089` n `13`; crypto_alt avg `-0.207` n `238`; crypto_major avg `0.5829` n `8`; equity avg `1.1665` n `156`; fx avg `0.1074` n `6`; index avg `0.2921` n `27`; metal avg `0.1331` n `20`; unknown avg `1.7291` n `1126`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
