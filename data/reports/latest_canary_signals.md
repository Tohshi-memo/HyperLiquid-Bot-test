# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T22:52:30.072028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0484` n `12`; crypto_alt avg `-0.184` n `228`; crypto_major avg `-0.1492` n `8`; equity avg `-0.2219` n `74`; fx avg `-0.0128` n `6`; index avg `-0.07` n `23`; metal avg `-0.3109` n `18`; unknown avg `-0.0531` n `547`
- 1h: commodity avg `0.1342` n `12`; crypto_alt avg `-0.0899` n `228`; crypto_major avg `-0.1384` n `8`; equity avg `-0.3898` n `74`; fx avg `0.0697` n `6`; index avg `-0.1542` n `23`; metal avg `-0.355` n `18`; unknown avg `-0.1316` n `547`
- 4h: commodity avg `0.4993` n `12`; crypto_alt avg `-0.2024` n `228`; crypto_major avg `-0.493` n `8`; equity avg `-0.4647` n `74`; fx avg `-0.0378` n `6`; index avg `0.3723` n `23`; metal avg `-0.5886` n `18`; unknown avg `-0.0084` n `547`
- 24h: commodity avg `-0.5437` n `12`; crypto_alt avg `-1.778` n `228`; crypto_major avg `-3.2007` n `8`; equity avg `-2.3724` n `74`; fx avg `0.0716` n `6`; index avg `-0.9732` n `23`; metal avg `-1.8606` n `18`; unknown avg `0.0009` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0366`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0365`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0363`, n `668`, weak_sample_signal
