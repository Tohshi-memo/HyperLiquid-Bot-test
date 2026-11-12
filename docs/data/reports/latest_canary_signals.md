# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T06:52:29.952072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0116` n `13`; crypto_alt avg `-0.1262` n `239`; crypto_major avg `-0.2515` n `8`; equity avg `-0.1689` n `161`; fx avg `0.0092` n `6`; index avg `-0.0212` n `27`; metal avg `-0.0235` n `20`; unknown avg `0.2008` n `1262`
- 1h: commodity avg `0.1795` n `13`; crypto_alt avg `-0.1491` n `239`; crypto_major avg `-0.2643` n `8`; equity avg `0.0722` n `161`; fx avg `0.0264` n `6`; index avg `-0.0293` n `27`; metal avg `-0.0601` n `20`; unknown avg `42.7534` n `1224`
- 4h: commodity avg `0.0599` n `13`; crypto_alt avg `-0.7322` n `239`; crypto_major avg `-0.912` n `8`; equity avg `-1.315` n `161`; fx avg `-0.011` n `6`; index avg `-0.1578` n `27`; metal avg `-0.0724` n `20`; unknown avg `0.1777` n `1204`
- 24h: commodity avg `0.1731` n `13`; crypto_alt avg `-1.3244` n `239`; crypto_major avg `-0.6244` n `8`; equity avg `-0.7424` n `161`; fx avg `-0.1387` n `6`; index avg `-0.1332` n `27`; metal avg `-0.6284` n `20`; unknown avg `-0.2785` n `1125`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
