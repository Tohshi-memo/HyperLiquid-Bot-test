# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T08:37:24.191446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0682` n `13`; crypto_alt avg `-0.1626` n `238`; crypto_major avg `-0.1821` n `8`; equity avg `-0.0186` n `156`; fx avg `0.0012` n `6`; index avg `-0.0104` n `27`; metal avg `-0.04` n `20`; unknown avg `0.3474` n `1261`
- 1h: commodity avg `0.0459` n `13`; crypto_alt avg `0.2257` n `238`; crypto_major avg `-0.0287` n `8`; equity avg `-0.3579` n `156`; fx avg `-0.0018` n `6`; index avg `-0.0579` n `27`; metal avg `-0.0162` n `20`; unknown avg `27.2936` n `1190`
- 4h: commodity avg `0.1899` n `13`; crypto_alt avg `0.4719` n `238`; crypto_major avg `-0.4761` n `8`; equity avg `-0.9571` n `156`; fx avg `-0.0034` n `6`; index avg `-0.0529` n `27`; metal avg `-0.2144` n `20`; unknown avg `1.7695` n `1172`
- 24h: commodity avg `0.1414` n `13`; crypto_alt avg `-3.1752` n `238`; crypto_major avg `-0.6689` n `8`; equity avg `-3.1137` n `155`; fx avg `0.1079` n `6`; index avg `-0.2986` n `27`; metal avg `-0.7389` n `20`; unknown avg `30.5599` n `938`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
