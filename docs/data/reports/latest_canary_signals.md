# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T23:22:28.735377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `13`; crypto_alt avg `-0.043` n `238`; crypto_major avg `-0.0402` n `8`; equity avg `0.0816` n `156`; fx avg `0.007` n `6`; index avg `0.0113` n `27`; metal avg `-0.0078` n `20`; unknown avg `0.2711` n `1261`
- 1h: commodity avg `-0.0041` n `13`; crypto_alt avg `0.4282` n `238`; crypto_major avg `0.2692` n `8`; equity avg `0.1475` n `156`; fx avg `-0.0007` n `6`; index avg `0.0114` n `27`; metal avg `-0.001` n `20`; unknown avg `0.1428` n `1255`
- 4h: commodity avg `-0.2604` n `13`; crypto_alt avg `1.6848` n `238`; crypto_major avg `0.5879` n `8`; equity avg `0.9434` n `156`; fx avg `-0.043` n `6`; index avg `0.1208` n `27`; metal avg `0.0972` n `20`; unknown avg `1.296` n `1149`
- 24h: commodity avg `0.0609` n `13`; crypto_alt avg `1.5312` n `238`; crypto_major avg `-0.8115` n `8`; equity avg `-2.5782` n `156`; fx avg `-0.1471` n `6`; index avg `-0.2322` n `27`; metal avg `-0.9103` n `20`; unknown avg `1.1031` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
