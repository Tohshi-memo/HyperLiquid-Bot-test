# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T13:37:32.245762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `-0.4632` n `233`; crypto_major avg `-0.3774` n `8`; equity avg `0.3388` n `134`; fx avg `0.0232` n `6`; index avg `0.0352` n `26`; metal avg `0.1079` n `20`; unknown avg `1.2721` n `799`
- 1h: commodity avg `-0.0328` n `12`; crypto_alt avg `-0.3524` n `233`; crypto_major avg `-0.3115` n `8`; equity avg `0.5552` n `134`; fx avg `0.0042` n `6`; index avg `0.0565` n `26`; metal avg `0.4979` n `20`; unknown avg `1.0332` n `796`
- 4h: commodity avg `0.0159` n `12`; crypto_alt avg `-0.3186` n `233`; crypto_major avg `-0.1368` n `8`; equity avg `0.1073` n `134`; fx avg `0.0328` n `6`; index avg `-0.0545` n `26`; metal avg `0.4131` n `20`; unknown avg `0.9271` n `790`
- 24h: commodity avg `0.141` n `12`; crypto_alt avg `1.0796` n `232`; crypto_major avg `1.9382` n `8`; equity avg `0.5202` n `134`; fx avg `-0.0568` n `6`; index avg `-0.1472` n `26`; metal avg `0.4184` n `20`; unknown avg `1.614` n `689`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
