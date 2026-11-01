# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T11:07:28.510375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0197` n `13`; crypto_alt avg `-0.0345` n `238`; crypto_major avg `-0.0829` n `8`; equity avg `-0.0075` n `156`; fx avg `-0.005` n `6`; index avg `-0.0021` n `27`; metal avg `-0.0003` n `20`; unknown avg `19.0079` n `1257`
- 1h: commodity avg `-0.0335` n `13`; crypto_alt avg `0.0245` n `238`; crypto_major avg `-0.0102` n `8`; equity avg `-0.0147` n `156`; fx avg `-0.0037` n `6`; index avg `0.004` n `27`; metal avg `0.019` n `20`; unknown avg `0.3433` n `1243`
- 4h: commodity avg `-0.0333` n `13`; crypto_alt avg `0.034` n `238`; crypto_major avg `0.0796` n `8`; equity avg `0.1117` n `156`; fx avg `-0.0068` n `6`; index avg `-0.0002` n `27`; metal avg `0.009` n `20`; unknown avg `0.5093` n `1227`
- 24h: commodity avg `-0.0897` n `13`; crypto_alt avg `0.8481` n `238`; crypto_major avg `0.5928` n `8`; equity avg `0.5256` n `156`; fx avg `-0.0287` n `6`; index avg `0.0348` n `27`; metal avg `0.0705` n `20`; unknown avg `3.8022` n `1004`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
