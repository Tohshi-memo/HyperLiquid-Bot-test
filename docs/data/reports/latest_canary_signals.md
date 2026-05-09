# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T19:52:11.784391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.0962` n `228`; crypto_major avg `0.1052` n `8`; equity avg `-0.0231` n `65`; fx avg `-0.0006` n `5`; index avg `-0.0253` n `23`; metal avg `0.037` n `18`; unknown avg `0.0255` n `376`
- 1h: commodity avg `0.0285` n `12`; crypto_alt avg `0.0874` n `228`; crypto_major avg `0.0872` n `8`; equity avg `-0.0418` n `65`; fx avg `-0.0066` n `5`; index avg `-0.0222` n `23`; metal avg `0.0441` n `18`; unknown avg `0.0448` n `376`
- 4h: commodity avg `0.0603` n `12`; crypto_alt avg `0.8726` n `228`; crypto_major avg `0.4771` n `8`; equity avg `0.1332` n `65`; fx avg `-0.0185` n `5`; index avg `0.0178` n `23`; metal avg `0.1187` n `18`; unknown avg `-0.1428` n `376`
- 24h: commodity avg `0.278` n `12`; crypto_alt avg `0.7312` n `228`; crypto_major avg `0.4977` n `8`; equity avg `1.0279` n `65`; fx avg `-0.033` n `5`; index avg `0.3691` n `23`; metal avg `-0.163` n `18`; unknown avg `0.218` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
