# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T15:37:28.811593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `0.0002` n `239`; crypto_major avg `0.0549` n `8`; equity avg `-0.0413` n `166`; fx avg `-0.0008` n `6`; index avg `0.0005` n `27`; metal avg `0.0088` n `20`; unknown avg `0.6452` n `1263`
- 1h: commodity avg `-0.0214` n `13`; crypto_alt avg `-0.0423` n `239`; crypto_major avg `0.3801` n `8`; equity avg `0.0289` n `166`; fx avg `0.0076` n `6`; index avg `-0.0007` n `27`; metal avg `0.0411` n `20`; unknown avg `261.0328` n `1259`
- 4h: commodity avg `-0.0506` n `13`; crypto_alt avg `-0.2388` n `239`; crypto_major avg `-0.0088` n `8`; equity avg `-0.0473` n `166`; fx avg `0.0145` n `6`; index avg `0.0466` n `27`; metal avg `0.0278` n `20`; unknown avg `0.4894` n `1247`
- 24h: commodity avg `-0.0092` n `13`; crypto_alt avg `0.4584` n `239`; crypto_major avg `1.1831` n `8`; equity avg `1.0226` n `166`; fx avg `-0.0188` n `6`; index avg `0.1771` n `27`; metal avg `0.0617` n `20`; unknown avg `-0.1621` n `1080`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
