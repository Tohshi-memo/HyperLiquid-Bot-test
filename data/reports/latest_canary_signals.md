# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T22:22:34.710887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0514` n `13`; crypto_alt avg `0.1262` n `238`; crypto_major avg `-0.013` n `8`; equity avg `0.0107` n `156`; fx avg `0.0091` n `6`; index avg `0.0034` n `27`; metal avg `0.0` n `20`; unknown avg `0.099` n `1261`
- 1h: commodity avg `0.0061` n `13`; crypto_alt avg `0.2487` n `238`; crypto_major avg `-0.1408` n `8`; equity avg `0.0437` n `156`; fx avg `-0.0226` n `6`; index avg `0.0314` n `27`; metal avg `0.0359` n `20`; unknown avg `199.1165` n `1255`
- 4h: commodity avg `-0.342` n `13`; crypto_alt avg `1.145` n `238`; crypto_major avg `0.1761` n `8`; equity avg `1.3539` n `156`; fx avg `-0.0326` n `6`; index avg `0.1478` n `27`; metal avg `0.1367` n `20`; unknown avg `0.7814` n `1149`
- 24h: commodity avg `0.0333` n `13`; crypto_alt avg `0.7514` n `238`; crypto_major avg `-1.5435` n `8`; equity avg `-2.9462` n `156`; fx avg `-0.1424` n `6`; index avg `-0.2614` n `27`; metal avg `-0.9643` n `20`; unknown avg `198.2829` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
