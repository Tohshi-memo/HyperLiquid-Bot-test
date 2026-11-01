# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T01:37:27.174564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `0.0965` n `238`; crypto_major avg `0.1028` n `8`; equity avg `0.0162` n `156`; fx avg `0.0012` n `6`; index avg `0.0001` n `27`; metal avg `0.0013` n `20`; unknown avg `-0.1096` n `1262`
- 1h: commodity avg `-0.0537` n `13`; crypto_alt avg `0.124` n `238`; crypto_major avg `0.0864` n `8`; equity avg `0.0484` n `156`; fx avg `0.0057` n `6`; index avg `0.0024` n `27`; metal avg `0.0051` n `20`; unknown avg `0.565` n `1256`
- 4h: commodity avg `0.0488` n `13`; crypto_alt avg `0.1217` n `238`; crypto_major avg `0.2577` n `8`; equity avg `0.0422` n `156`; fx avg `0.0048` n `6`; index avg `-0.0168` n `27`; metal avg `0.0168` n `20`; unknown avg `1.251` n `1112`
- 24h: commodity avg `0.0788` n `13`; crypto_alt avg `-0.6681` n `238`; crypto_major avg `-0.3473` n `8`; equity avg `-0.0015` n `156`; fx avg `0.0131` n `6`; index avg `-0.0847` n `27`; metal avg `0.0403` n `20`; unknown avg `1.8317` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
