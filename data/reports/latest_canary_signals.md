# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T14:37:31.697323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1154` n `12`; crypto_alt avg `-0.6695` n `234`; crypto_major avg `-0.4519` n `8`; equity avg `-0.4948` n `141`; fx avg `0.007` n `6`; index avg `-0.061` n `26`; metal avg `-0.0546` n `20`; unknown avg `1.4218` n `952`
- 1h: commodity avg `0.0545` n `12`; crypto_alt avg `-1.2959` n `234`; crypto_major avg `-0.7978` n `8`; equity avg `-0.7733` n `141`; fx avg `0.0314` n `6`; index avg `-0.0848` n `26`; metal avg `-0.0557` n `20`; unknown avg `82.9725` n `910`
- 4h: commodity avg `-0.1914` n `12`; crypto_alt avg `-0.3168` n `234`; crypto_major avg `-0.0278` n `8`; equity avg `-0.5459` n `141`; fx avg `-0.0017` n `6`; index avg `-0.0317` n `26`; metal avg `-0.1477` n `20`; unknown avg `50.265` n `904`
- 24h: commodity avg `-0.1818` n `12`; crypto_alt avg `-3.3016` n `234`; crypto_major avg `-2.016` n `8`; equity avg `-3.2719` n `141`; fx avg `0.0343` n `6`; index avg `-0.2908` n `26`; metal avg `-1.011` n `20`; unknown avg `7.6106` n `786`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.201`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
