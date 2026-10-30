# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T12:37:29.686893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0443` n `13`; crypto_alt avg `0.1688` n `238`; crypto_major avg `0.0696` n `8`; equity avg `-0.0557` n `156`; fx avg `-0.0131` n `6`; index avg `0.0096` n `27`; metal avg `0.0336` n `20`; unknown avg `0.0814` n `1261`
- 1h: commodity avg `-0.1024` n `13`; crypto_alt avg `-0.1088` n `238`; crypto_major avg `-0.1955` n `8`; equity avg `-0.2856` n `156`; fx avg `-0.01` n `6`; index avg `-0.0295` n `27`; metal avg `-0.119` n `20`; unknown avg `0.4865` n `1249`
- 4h: commodity avg `-0.0704` n `13`; crypto_alt avg `0.565` n `238`; crypto_major avg `-0.1794` n `8`; equity avg `-0.9497` n `156`; fx avg `-0.0229` n `6`; index avg `-0.0911` n `27`; metal avg `-0.1651` n `20`; unknown avg `5.0571` n `1249`
- 24h: commodity avg `0.2381` n `13`; crypto_alt avg `-3.8081` n `238`; crypto_major avg `-2.3511` n `8`; equity avg `-3.9618` n `156`; fx avg `0.0285` n `6`; index avg `-0.4177` n `27`; metal avg `-0.743` n `20`; unknown avg `23.1008` n `1032`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
