# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T11:22:29.968564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0011` n `13`; crypto_alt avg `-0.0081` n `238`; crypto_major avg `0.0242` n `8`; equity avg `0.0078` n `156`; fx avg `0.0056` n `6`; index avg `0.0013` n `27`; metal avg `0.0027` n `20`; unknown avg `-0.0451` n `1261`
- 1h: commodity avg `-0.0361` n `13`; crypto_alt avg `-0.1904` n `238`; crypto_major avg `-0.1519` n `8`; equity avg `-0.0492` n `156`; fx avg `0.0056` n `6`; index avg `0.0048` n `27`; metal avg `0.016` n `20`; unknown avg `0.1205` n `1257`
- 4h: commodity avg `-0.0307` n `13`; crypto_alt avg `0.0937` n `238`; crypto_major avg `0.3434` n `8`; equity avg `0.1795` n `156`; fx avg `0.0016` n `6`; index avg `0.0118` n `27`; metal avg `0.024` n `20`; unknown avg `0.371` n `1227`
- 24h: commodity avg `-0.0933` n `13`; crypto_alt avg `0.5565` n `238`; crypto_major avg `0.5208` n `8`; equity avg `0.5098` n `156`; fx avg `-0.0235` n `6`; index avg `0.0345` n `27`; metal avg `0.071` n `20`; unknown avg `3.7491` n `1014`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
