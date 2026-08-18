# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T06:07:30.419544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1228` n `12`; crypto_alt avg `-0.0548` n `230`; crypto_major avg `-0.0572` n `8`; equity avg `-0.3043` n `114`; fx avg `-0.0048` n `6`; index avg `-0.0839` n `25`; metal avg `-0.0536` n `20`; unknown avg `-0.0336` n `761`
- 1h: commodity avg `0.0435` n `12`; crypto_alt avg `-0.1726` n `230`; crypto_major avg `-0.1806` n `8`; equity avg `-0.4399` n `114`; fx avg `-0.0242` n `6`; index avg `-0.1423` n `25`; metal avg `-0.0247` n `20`; unknown avg `-0.0429` n `761`
- 4h: commodity avg `0.0727` n `12`; crypto_alt avg `-0.7222` n `230`; crypto_major avg `-0.1763` n `8`; equity avg `-1.0926` n `114`; fx avg `-0.0121` n `6`; index avg `-0.3119` n `25`; metal avg `-0.0953` n `20`; unknown avg `-0.1201` n `761`
- 24h: commodity avg `0.8097` n `12`; crypto_alt avg `-1.4296` n `230`; crypto_major avg `-0.0858` n `8`; equity avg `-1.8704` n `114`; fx avg `-0.0366` n `6`; index avg `-0.4991` n `25`; metal avg `-0.3137` n `20`; unknown avg `0.0263` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1914`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
