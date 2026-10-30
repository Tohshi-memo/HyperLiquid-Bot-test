# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T20:07:32.966040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0747` n `13`; crypto_alt avg `0.044` n `238`; crypto_major avg `-0.0321` n `8`; equity avg `-0.0219` n `156`; fx avg `-0.0204` n `6`; index avg `0.0174` n `27`; metal avg `0.0347` n `20`; unknown avg `0.081` n `1219`
- 1h: commodity avg `-0.2514` n `13`; crypto_alt avg `0.8265` n `238`; crypto_major avg `0.4919` n `8`; equity avg `0.9432` n `156`; fx avg `-0.014` n `6`; index avg `0.1183` n `27`; metal avg `0.1477` n `20`; unknown avg `1.0595` n `1219`
- 4h: commodity avg `-0.2704` n `13`; crypto_alt avg `0.1336` n `238`; crypto_major avg `-0.2707` n `8`; equity avg `-0.021` n `156`; fx avg `-0.0186` n `6`; index avg `0.0011` n `27`; metal avg `-0.0098` n `20`; unknown avg `0.5278` n `1221`
- 24h: commodity avg `0.0529` n `13`; crypto_alt avg `-2.752` n `238`; crypto_major avg `-3.002` n `8`; equity avg `-3.9014` n `156`; fx avg `-0.0951` n `6`; index avg `-0.312` n `27`; metal avg `-0.9617` n `20`; unknown avg `180.4443` n `1028`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
