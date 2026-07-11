# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T00:52:26.179437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `0.155` n `229`; crypto_major avg `0.0909` n `8`; equity avg `0.0137` n `92`; fx avg `0.0005` n `6`; index avg `-0.0018` n `25`; metal avg `0.0058` n `20`; unknown avg `0.1577` n `765`
- 1h: commodity avg `0.0344` n `12`; crypto_alt avg `-0.0237` n `229`; crypto_major avg `-0.0609` n `8`; equity avg `-0.0142` n `92`; fx avg `0.0006` n `6`; index avg `-0.0039` n `25`; metal avg `0.0045` n `20`; unknown avg `1.482` n `765`
- 4h: commodity avg `0.0137` n `12`; crypto_alt avg `0.4497` n `229`; crypto_major avg `0.1615` n `8`; equity avg `0.0575` n `92`; fx avg `0.0071` n `6`; index avg `-0.023` n `25`; metal avg `-0.0027` n `20`; unknown avg `1.1486` n `765`
- 24h: commodity avg `-0.2428` n `12`; crypto_alt avg `1.3405` n `229`; crypto_major avg `1.1969` n `8`; equity avg `-0.4072` n `92`; fx avg `-0.1934` n `6`; index avg `0.1349` n `25`; metal avg `0.1484` n `20`; unknown avg `1.0511` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
