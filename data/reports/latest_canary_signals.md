# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T19:07:31.420725+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `-0.0548` n `238`; crypto_major avg `-0.0568` n `8`; equity avg `0.0087` n `156`; fx avg `-0.0007` n `6`; index avg `-0.0028` n `27`; metal avg `-0.0024` n `20`; unknown avg `11.8303` n `1257`
- 1h: commodity avg `0.0184` n `13`; crypto_alt avg `-0.5434` n `238`; crypto_major avg `-0.2434` n `8`; equity avg `-0.1246` n `156`; fx avg `0.0115` n `6`; index avg `-0.0271` n `27`; metal avg `-0.0019` n `20`; unknown avg `0.2045` n `1249`
- 4h: commodity avg `-0.0617` n `13`; crypto_alt avg `-1.0818` n `238`; crypto_major avg `-0.537` n `8`; equity avg `-0.154` n `156`; fx avg `0.012` n `6`; index avg `-0.0139` n `27`; metal avg `0.0031` n `20`; unknown avg `0.1036` n `1235`
- 24h: commodity avg `0.0322` n `13`; crypto_alt avg `-0.991` n `238`; crypto_major avg `-0.3999` n `8`; equity avg `0.2276` n `156`; fx avg `0.0216` n `6`; index avg `0.0663` n `27`; metal avg `0.0524` n `20`; unknown avg `3.9193` n `1004`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
