# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T13:22:22.542403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `13`; crypto_alt avg `-0.0219` n `238`; crypto_major avg `-0.161` n `8`; equity avg `-0.0368` n `156`; fx avg `0.0024` n `6`; index avg `-0.0084` n `27`; metal avg `0.0025` n `20`; unknown avg `0.0619` n `1260`
- 1h: commodity avg `-0.0534` n `13`; crypto_alt avg `-0.1447` n `238`; crypto_major avg `-0.2024` n `8`; equity avg `-0.0987` n `156`; fx avg `-0.0066` n `6`; index avg `-0.0164` n `27`; metal avg `0.0057` n `20`; unknown avg `0.2927` n `1256`
- 4h: commodity avg `-0.0525` n `13`; crypto_alt avg `0.1818` n `238`; crypto_major avg `0.1724` n `8`; equity avg `-0.126` n `156`; fx avg `0.0034` n `6`; index avg `-0.0173` n `27`; metal avg `0.0164` n `20`; unknown avg `206.348` n `1218`
- 24h: commodity avg `-0.1242` n `13`; crypto_alt avg `0.6406` n `238`; crypto_major avg `-0.4777` n `8`; equity avg `-1.1131` n `156`; fx avg `-0.011` n `6`; index avg `-0.138` n `27`; metal avg `-0.1683` n `20`; unknown avg `3.5277` n `1045`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
