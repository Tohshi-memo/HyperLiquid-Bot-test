# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T09:22:16.264084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.1014` n `228`; crypto_major avg `-0.0611` n `8`; equity avg `-0.0115` n `65`; fx avg `0.0043` n `5`; index avg `-0.005` n `23`; metal avg `0.0144` n `18`; unknown avg `-0.1653` n `376`
- 1h: commodity avg `-0.0573` n `12`; crypto_alt avg `0.1018` n `228`; crypto_major avg `0.1729` n `8`; equity avg `0.0183` n `65`; fx avg `0.006` n `5`; index avg `-0.0006` n `23`; metal avg `0.0388` n `18`; unknown avg `0.0336` n `376`
- 4h: commodity avg `-0.1628` n `12`; crypto_alt avg `0.5347` n `228`; crypto_major avg `0.3739` n `8`; equity avg `0.0285` n `65`; fx avg `0.0115` n `5`; index avg `-0.015` n `23`; metal avg `-0.0042` n `18`; unknown avg `0.0141` n `366`
- 24h: commodity avg `0.0255` n `12`; crypto_alt avg `-0.0258` n `228`; crypto_major avg `-0.0316` n `8`; equity avg `0.9851` n `65`; fx avg `-0.015` n `5`; index avg `0.2025` n `23`; metal avg `0.3745` n `18`; unknown avg `0.0685` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
