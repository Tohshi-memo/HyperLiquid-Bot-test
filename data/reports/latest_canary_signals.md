# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T12:52:31.977269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0587` n `12`; crypto_alt avg `-0.0487` n `228`; crypto_major avg `0.0271` n `8`; equity avg `0.0259` n `86`; fx avg `0.0018` n `6`; index avg `0.0158` n `23`; metal avg `0.1711` n `20`; unknown avg `0.021` n `765`
- 1h: commodity avg `0.0609` n `12`; crypto_alt avg `0.1333` n `228`; crypto_major avg `0.3875` n `8`; equity avg `0.2171` n `86`; fx avg `0.026` n `6`; index avg `0.063` n `23`; metal avg `0.3631` n `20`; unknown avg `0.0254` n `765`
- 4h: commodity avg `0.1199` n `12`; crypto_alt avg `-0.7229` n `228`; crypto_major avg `-0.7529` n `8`; equity avg `0.2716` n `86`; fx avg `-0.0271` n `6`; index avg `0.0683` n `23`; metal avg `0.3775` n `20`; unknown avg `-0.1701` n `765`
- 24h: commodity avg `-0.0451` n `12`; crypto_alt avg `-1.6174` n `228`; crypto_major avg `-1.2753` n `8`; equity avg `0.5775` n `86`; fx avg `0.0293` n `6`; index avg `0.5692` n `23`; metal avg `0.0033` n `20`; unknown avg `-0.6193` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
