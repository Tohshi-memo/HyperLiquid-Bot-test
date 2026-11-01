# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T10:37:27.739179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `13`; crypto_alt avg `-0.1766` n `238`; crypto_major avg `-0.0964` n `8`; equity avg `0.0015` n `156`; fx avg `0.0037` n `6`; index avg `-0.0022` n `27`; metal avg `0.0211` n `20`; unknown avg `0.1286` n `1263`
- 1h: commodity avg `-0.0294` n `13`; crypto_alt avg `0.2201` n `238`; crypto_major avg `0.2037` n `8`; equity avg `0.0619` n `156`; fx avg `-0.0012` n `6`; index avg `-0.0047` n `27`; metal avg `0.0285` n `20`; unknown avg `0.1589` n `1243`
- 4h: commodity avg `-0.0211` n `13`; crypto_alt avg `0.0385` n `238`; crypto_major avg `0.2566` n `8`; equity avg `0.1995` n `156`; fx avg `-0.016` n `6`; index avg `0.0129` n `27`; metal avg `0.0184` n `20`; unknown avg `0.7282` n `1227`
- 24h: commodity avg `-0.0406` n `13`; crypto_alt avg `0.7254` n `238`; crypto_major avg `0.5387` n `8`; equity avg `0.5591` n `156`; fx avg `-0.0267` n `6`; index avg `0.0272` n `27`; metal avg `0.0768` n `20`; unknown avg `1.8605` n `990`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
