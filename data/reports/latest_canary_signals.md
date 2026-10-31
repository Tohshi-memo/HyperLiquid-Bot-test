# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T23:37:30.574502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `13`; crypto_alt avg `-0.0112` n `238`; crypto_major avg `0.0308` n `8`; equity avg `-0.0003` n `156`; fx avg `0.0012` n `6`; index avg `-0.0098` n `27`; metal avg `0.0006` n `20`; unknown avg `113.5099` n `1260`
- 1h: commodity avg `-0.0064` n `13`; crypto_alt avg `-0.1184` n `238`; crypto_major avg `-0.2193` n `8`; equity avg `-0.0439` n `156`; fx avg `0.0023` n `6`; index avg `-0.0058` n `27`; metal avg `-0.0063` n `20`; unknown avg `0.4605` n `1232`
- 4h: commodity avg `0.0405` n `13`; crypto_alt avg `-0.2632` n `238`; crypto_major avg `-0.2366` n `8`; equity avg `-0.0482` n `156`; fx avg `0.0138` n `6`; index avg `-0.007` n `27`; metal avg `0.0107` n `20`; unknown avg `2.4858` n `1088`
- 24h: commodity avg `-0.0704` n `13`; crypto_alt avg `-0.8299` n `238`; crypto_major avg `-0.4494` n `8`; equity avg `-0.0011` n `156`; fx avg `0.014` n `6`; index avg `-0.0587` n `27`; metal avg `0.0472` n `20`; unknown avg `0.9043` n `1030`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
