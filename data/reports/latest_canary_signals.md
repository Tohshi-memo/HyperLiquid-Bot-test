# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T20:22:29.238146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `12`; crypto_alt avg `0.1197` n `232`; crypto_major avg `0.1479` n `8`; equity avg `0.1835` n `131`; fx avg `-0.0022` n `6`; index avg `0.0197` n `26`; metal avg `-0.0002` n `20`; unknown avg `-0.0032` n `783`
- 1h: commodity avg `0.0477` n `12`; crypto_alt avg `0.0823` n `232`; crypto_major avg `-0.0101` n `8`; equity avg `0.037` n `131`; fx avg `0.0064` n `6`; index avg `0.0078` n `26`; metal avg `-0.0402` n `20`; unknown avg `0.0424` n `781`
- 4h: commodity avg `0.3292` n `12`; crypto_alt avg `-0.1988` n `232`; crypto_major avg `-0.3947` n `8`; equity avg `-0.2057` n `131`; fx avg `0.002` n `6`; index avg `-0.0984` n `26`; metal avg `-0.2893` n `20`; unknown avg `-0.4967` n `781`
- 24h: commodity avg `0.8887` n `12`; crypto_alt avg `-0.3795` n `232`; crypto_major avg `-2.1986` n `8`; equity avg `-1.8121` n `130`; fx avg `0.0448` n `6`; index avg `-0.3346` n `26`; metal avg `-0.8937` n `20`; unknown avg `0.2025` n `754`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0419`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0378`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0317`, n `668`, weak_sample_signal
