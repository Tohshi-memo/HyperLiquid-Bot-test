# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T07:22:27.433974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `-0.1869` n `233`; crypto_major avg `-0.092` n `8`; equity avg `-0.0036` n `134`; fx avg `0.0121` n `6`; index avg `0.0061` n `26`; metal avg `-0.0255` n `20`; unknown avg `-0.1309` n `797`
- 1h: commodity avg `0.0898` n `12`; crypto_alt avg `-0.0258` n `233`; crypto_major avg `-0.13` n `8`; equity avg `0.029` n `134`; fx avg `0.0287` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0652` n `20`; unknown avg `0.3938` n `793`
- 4h: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.4129` n `233`; crypto_major avg `-0.6041` n `8`; equity avg `0.1585` n `134`; fx avg `0.0172` n `6`; index avg `0.0745` n `26`; metal avg `-0.0534` n `20`; unknown avg `0.2347` n `765`
- 24h: commodity avg `-0.1355` n `12`; crypto_alt avg `-4.3185` n `233`; crypto_major avg `-3.1861` n `8`; equity avg `-1.1416` n `134`; fx avg `0.0582` n `6`; index avg `-0.127` n `26`; metal avg `0.1219` n `20`; unknown avg `0.3822` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
