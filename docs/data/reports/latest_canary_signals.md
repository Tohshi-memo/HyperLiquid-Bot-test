# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T10:22:29.930209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `13`; crypto_alt avg `0.2074` n `238`; crypto_major avg `0.1661` n `8`; equity avg `0.0423` n `156`; fx avg `-0.0037` n `6`; index avg `0.0005` n `27`; metal avg `0.0057` n `20`; unknown avg `-0.0001` n `1247`
- 1h: commodity avg `-0.0079` n `13`; crypto_alt avg `0.3143` n `238`; crypto_major avg `0.1994` n `8`; equity avg `0.031` n `156`; fx avg `-0.0049` n `6`; index avg `-0.0081` n `27`; metal avg `0.0054` n `20`; unknown avg `0.0187` n `1243`
- 4h: commodity avg `-0.024` n `13`; crypto_alt avg `0.0784` n `238`; crypto_major avg `0.2765` n `8`; equity avg `0.2076` n `156`; fx avg `-0.0208` n `6`; index avg `0.0181` n `27`; metal avg `0.022` n `20`; unknown avg `0.5696` n `1225`
- 24h: commodity avg `-0.0082` n `13`; crypto_alt avg `0.9426` n `238`; crypto_major avg `0.7397` n `8`; equity avg `0.5422` n `156`; fx avg `-0.034` n `6`; index avg `0.023` n `27`; metal avg `0.0556` n `20`; unknown avg `1.6341` n `990`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
