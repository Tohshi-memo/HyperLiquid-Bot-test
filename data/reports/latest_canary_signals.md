# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T07:37:25.831040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0506` n `12`; crypto_alt avg `-0.2712` n `233`; crypto_major avg `-0.2468` n `8`; equity avg `-0.0978` n `134`; fx avg `-0.007` n `6`; index avg `-0.0284` n `26`; metal avg `-0.0395` n `20`; unknown avg `0.6773` n `797`
- 1h: commodity avg `0.1538` n `12`; crypto_alt avg `-0.4367` n `233`; crypto_major avg `-0.4425` n `8`; equity avg `-0.1136` n `134`; fx avg `0.0215` n `6`; index avg `-0.0391` n `26`; metal avg `-0.1045` n `20`; unknown avg `0.3757` n `793`
- 4h: commodity avg `0.0352` n `12`; crypto_alt avg `-0.5874` n `233`; crypto_major avg `-0.737` n `8`; equity avg `0.08` n `134`; fx avg `0.0225` n `6`; index avg `0.045` n `26`; metal avg `-0.0775` n `20`; unknown avg `0.2255` n `765`
- 24h: commodity avg `-0.0143` n `12`; crypto_alt avg `-4.5565` n `233`; crypto_major avg `-3.3953` n `8`; equity avg `-1.2541` n `134`; fx avg `0.0718` n `6`; index avg `-0.1588` n `26`; metal avg `0.047` n `20`; unknown avg `0.5325` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
