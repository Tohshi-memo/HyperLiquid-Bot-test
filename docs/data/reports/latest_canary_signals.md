# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T01:37:24.376776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0431` n `12`; crypto_alt avg `0.0451` n `229`; crypto_major avg `-0.072` n `8`; equity avg `-0.0127` n `92`; fx avg `-0.005` n `6`; index avg `-0.0008` n `25`; metal avg `0.0088` n `20`; unknown avg `0.0642` n `765`
- 1h: commodity avg `-0.0498` n `12`; crypto_alt avg `0.3441` n `229`; crypto_major avg `0.2318` n `8`; equity avg `0.0402` n `92`; fx avg `-0.0006` n `6`; index avg `-0.0004` n `25`; metal avg `0.0107` n `20`; unknown avg `0.5255` n `765`
- 4h: commodity avg `-0.0021` n `12`; crypto_alt avg `0.2032` n `229`; crypto_major avg `0.0698` n `8`; equity avg `0.0823` n `92`; fx avg `-0.0028` n `6`; index avg `-0.0172` n `25`; metal avg `0.012` n `20`; unknown avg `3.1236` n `765`
- 24h: commodity avg `-0.3192` n `12`; crypto_alt avg `0.9343` n `229`; crypto_major avg `0.7334` n `8`; equity avg `-0.7642` n `92`; fx avg `-0.2116` n `6`; index avg `0.0326` n `25`; metal avg `0.1268` n `20`; unknown avg `3.8191` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
