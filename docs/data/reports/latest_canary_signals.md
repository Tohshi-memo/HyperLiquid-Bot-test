# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T08:19:55.941946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.1021` n `228`; crypto_major avg `-0.1964` n `8`; equity avg `-0.01` n `88`; fx avg `0.0096` n `6`; index avg `-0.0058` n `23`; metal avg `-0.0026` n `20`; unknown avg `0.0272` n `764`
- 1h: commodity avg `0.0344` n `12`; crypto_alt avg `-0.2222` n `228`; crypto_major avg `-0.0912` n `8`; equity avg `0.0615` n `88`; fx avg `-0.0081` n `6`; index avg `-0.0001` n `23`; metal avg `-0.0069` n `20`; unknown avg `0.0149` n `748`
- 4h: commodity avg `0.049` n `12`; crypto_alt avg `-0.5281` n `228`; crypto_major avg `-0.3721` n `8`; equity avg `0.1462` n `88`; fx avg `0.0131` n `6`; index avg `-0.0024` n `23`; metal avg `-0.0278` n `20`; unknown avg `-0.2521` n `716`
- 24h: commodity avg `0.0383` n `12`; crypto_alt avg `0.8573` n `228`; crypto_major avg `0.5982` n `8`; equity avg `1.4834` n `87`; fx avg `0.0415` n `6`; index avg `0.0198` n `23`; metal avg `0.6209` n `20`; unknown avg `-0.1727` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2049`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
