# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T23:37:14.747750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0275` n `12`; crypto_alt avg `-0.0599` n `228`; crypto_major avg `0.0113` n `8`; equity avg `0.0416` n `65`; fx avg `0.0` n `5`; index avg `-0.0013` n `23`; metal avg `0.0018` n `18`; unknown avg `0.1817` n `376`
- 1h: commodity avg `-0.0295` n `12`; crypto_alt avg `-0.3051` n `228`; crypto_major avg `-0.1386` n `8`; equity avg `0.0291` n `65`; fx avg `0.0` n `5`; index avg `0.04` n `23`; metal avg `-0.0172` n `18`; unknown avg `0.2813` n `376`
- 4h: commodity avg `-0.0605` n `12`; crypto_alt avg `-0.2931` n `228`; crypto_major avg `-0.1989` n `8`; equity avg `0.4114` n `65`; fx avg `-0.0015` n `5`; index avg `0.1134` n `23`; metal avg `0.1366` n `18`; unknown avg `0.3185` n `376`
- 24h: commodity avg `0.4048` n `12`; crypto_alt avg `-0.0115` n `228`; crypto_major avg `0.3592` n `8`; equity avg `0.7905` n `65`; fx avg `-0.0244` n `5`; index avg `0.3333` n `23`; metal avg `0.3577` n `18`; unknown avg `0.2117` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
