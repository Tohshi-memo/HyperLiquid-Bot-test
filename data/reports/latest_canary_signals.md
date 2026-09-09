# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T12:22:32.764337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `0.0941` n `233`; crypto_major avg `0.1189` n `8`; equity avg `0.0203` n `134`; fx avg `0.0018` n `6`; index avg `0.0012` n `26`; metal avg `-0.046` n `20`; unknown avg `-0.0183` n `798`
- 1h: commodity avg `-0.0732` n `12`; crypto_alt avg `0.6845` n `233`; crypto_major avg `0.6979` n `8`; equity avg `-0.0139` n `134`; fx avg `0.004` n `6`; index avg `-0.0154` n `26`; metal avg `-0.0883` n `20`; unknown avg `0.5357` n `796`
- 4h: commodity avg `0.0992` n `12`; crypto_alt avg `-0.5295` n `233`; crypto_major avg `-0.3104` n `8`; equity avg `-0.8771` n `134`; fx avg `0.0193` n `6`; index avg `-0.2016` n `26`; metal avg `-0.1264` n `20`; unknown avg `14.1391` n `790`
- 24h: commodity avg `-0.0885` n `12`; crypto_alt avg `0.67` n `232`; crypto_major avg `1.7218` n `8`; equity avg `0.2305` n `134`; fx avg `-0.0871` n `6`; index avg `-0.1656` n `26`; metal avg `-0.0083` n `20`; unknown avg `1.2365` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
