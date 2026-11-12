# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T18:26:26.339319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `13`; crypto_alt avg `-0.0066` n `239`; crypto_major avg `0.0217` n `8`; equity avg `0.0905` n `162`; fx avg `0.0073` n `6`; index avg `0.0049` n `27`; metal avg `0.0176` n `20`; unknown avg `-0.2382` n `1257`
- 1h: commodity avg `0.1775` n `13`; crypto_alt avg `0.3184` n `239`; crypto_major avg `0.268` n `8`; equity avg `0.3186` n `162`; fx avg `-0.0048` n `6`; index avg `0.0219` n `27`; metal avg `0.0618` n `20`; unknown avg `0.4089` n `1253`
- 4h: commodity avg `0.3981` n `13`; crypto_alt avg `0.8022` n `239`; crypto_major avg `0.9772` n `8`; equity avg `2.1181` n `162`; fx avg `-0.0614` n `6`; index avg `0.1986` n `27`; metal avg `-0.1228` n `20`; unknown avg `47.5205` n `1229`
- 24h: commodity avg `0.4648` n `13`; crypto_alt avg `-3.2641` n `239`; crypto_major avg `-3.4224` n `8`; equity avg `-3.0103` n `162`; fx avg `-0.1494` n `6`; index avg `-0.1671` n `27`; metal avg `-0.7773` n `20`; unknown avg `4.0829` n `1137`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
