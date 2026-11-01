# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T10:52:37.839259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `13`; crypto_alt avg `0.0286` n `238`; crypto_major avg `0.0032` n `8`; equity avg `-0.0509` n `156`; fx avg `0.0012` n `6`; index avg `0.0079` n `27`; metal avg `-0.0076` n `20`; unknown avg `0.0326` n `1261`
- 1h: commodity avg `-0.0188` n `13`; crypto_alt avg `0.0309` n `238`; crypto_major avg `0.078` n `8`; equity avg `0.0011` n `156`; fx avg `0.0006` n `6`; index avg `-0.0052` n `27`; metal avg `0.0209` n `20`; unknown avg `0.2023` n `1243`
- 4h: commodity avg `-0.0106` n `13`; crypto_alt avg `0.06` n `238`; crypto_major avg `0.142` n `8`; equity avg `0.1445` n `156`; fx avg `-0.0043` n `6`; index avg `0.0118` n `27`; metal avg `0.01` n `20`; unknown avg `0.7246` n `1227`
- 24h: commodity avg `-0.0609` n `13`; crypto_alt avg `0.8353` n `238`; crypto_major avg `0.6555` n `8`; equity avg `0.5225` n `156`; fx avg `-0.027` n `6`; index avg `0.0363` n `27`; metal avg `0.0658` n `20`; unknown avg `3.9526` n `992`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
