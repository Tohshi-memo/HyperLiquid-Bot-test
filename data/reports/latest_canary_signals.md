# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T01:28:39.916369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `13`; crypto_alt avg `-0.0848` n `238`; crypto_major avg `-0.0714` n `8`; equity avg `0.0106` n `156`; fx avg `-0.0035` n `6`; index avg `0.0002` n `27`; metal avg `0.0051` n `20`; unknown avg `-0.0855` n `1260`
- 1h: commodity avg `-0.0597` n `13`; crypto_alt avg `0.1933` n `238`; crypto_major avg `0.2055` n `8`; equity avg `0.0517` n `156`; fx avg `0.0077` n `6`; index avg `-0.029` n `27`; metal avg `0.0044` n `20`; unknown avg `1.3308` n `1240`
- 4h: commodity avg `0.0529` n `13`; crypto_alt avg `0.0266` n `238`; crypto_major avg `0.1993` n `8`; equity avg `0.026` n `156`; fx avg `0.0036` n `6`; index avg `-0.0168` n `27`; metal avg `0.0178` n `20`; unknown avg `1.4242` n `1098`
- 24h: commodity avg `0.0661` n `13`; crypto_alt avg `-0.6611` n `238`; crypto_major avg `-0.3593` n `8`; equity avg `-0.0214` n `156`; fx avg `0.0015` n `6`; index avg `-0.0867` n `27`; metal avg `0.0457` n `20`; unknown avg `1.897` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
