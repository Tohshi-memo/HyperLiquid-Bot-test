# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T06:22:26.136133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0491` n `12`; crypto_alt avg `0.4429` n `228`; crypto_major avg `0.5727` n `8`; equity avg `0.2057` n `74`; fx avg `0.0009` n `6`; index avg `0.0804` n `23`; metal avg `0.1058` n `18`; unknown avg `0.2636` n `425`
- 1h: commodity avg `0.095` n `12`; crypto_alt avg `1.5615` n `228`; crypto_major avg `1.439` n `8`; equity avg `0.7185` n `74`; fx avg `-0.0032` n `6`; index avg `0.3555` n `23`; metal avg `0.3467` n `18`; unknown avg `0.0946` n `415`
- 4h: commodity avg `-0.3313` n `12`; crypto_alt avg `-0.7498` n `228`; crypto_major avg `0.3047` n `8`; equity avg `0.3286` n `74`; fx avg `-0.007` n `6`; index avg `0.0326` n `23`; metal avg `-0.1819` n `18`; unknown avg `-0.1424` n `415`
- 24h: commodity avg `-1.4021` n `12`; crypto_alt avg `-2.4218` n `228`; crypto_major avg `-1.1113` n `8`; equity avg `-5.8636` n `74`; fx avg `-0.2136` n `6`; index avg `-3.9514` n `23`; metal avg `-3.5997` n `18`; unknown avg `0.1083` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
