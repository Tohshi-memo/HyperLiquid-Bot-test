# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T15:07:27.839579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `12`; crypto_alt avg `0.0884` n `232`; crypto_major avg `0.0163` n `8`; equity avg `0.0278` n `134`; fx avg `0.0075` n `6`; index avg `0.0097` n `26`; metal avg `0.0004` n `20`; unknown avg `0.0537` n `792`
- 1h: commodity avg `0.0129` n `12`; crypto_alt avg `0.1809` n `232`; crypto_major avg `0.1708` n `8`; equity avg `0.0427` n `134`; fx avg `0.0071` n `6`; index avg `0.0168` n `26`; metal avg `-0.0037` n `20`; unknown avg `-0.28` n `792`
- 4h: commodity avg `0.0479` n `12`; crypto_alt avg `0.2287` n `232`; crypto_major avg `0.7881` n `8`; equity avg `0.0628` n `134`; fx avg `0.0163` n `6`; index avg `0.0146` n `26`; metal avg `-0.0034` n `20`; unknown avg `-0.4011` n `729`
- 24h: commodity avg `0.1123` n `12`; crypto_alt avg `3.0533` n `232`; crypto_major avg `2.2407` n `8`; equity avg `0.6354` n `134`; fx avg `0.0088` n `6`; index avg `0.0719` n `26`; metal avg `-0.015` n `20`; unknown avg `0.3069` n `656`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
