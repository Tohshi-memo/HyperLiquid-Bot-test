# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T21:07:29.223307+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `0.0173` n `238`; crypto_major avg `0.025` n `8`; equity avg `0.025` n `156`; fx avg `-0.0022` n `6`; index avg `-0.011` n `27`; metal avg `-0.0034` n `20`; unknown avg `4.2784` n `1249`
- 1h: commodity avg `-0.0142` n `13`; crypto_alt avg `0.1988` n `238`; crypto_major avg `0.1677` n `8`; equity avg `0.0988` n `156`; fx avg `-0.0088` n `6`; index avg `-0.0003` n `27`; metal avg `0.0125` n `20`; unknown avg `3.9569` n `1249`
- 4h: commodity avg `0.0342` n `13`; crypto_alt avg `-0.5962` n `238`; crypto_major avg `-0.3346` n `8`; equity avg `-0.1534` n `156`; fx avg `-0.0019` n `6`; index avg `-0.0543` n `27`; metal avg `-0.0225` n `20`; unknown avg `166.5046` n `1207`
- 24h: commodity avg `0.0201` n `13`; crypto_alt avg `-0.5557` n `238`; crypto_major avg `-0.0921` n `8`; equity avg `0.3056` n `156`; fx avg `0.0071` n `6`; index avg `0.0433` n `27`; metal avg `0.046` n `20`; unknown avg `4.838` n `988`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
