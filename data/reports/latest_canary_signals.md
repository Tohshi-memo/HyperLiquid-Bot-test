# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T09:52:33.475645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `-0.2164` n `228`; crypto_major avg `-0.1534` n `8`; equity avg `-0.0313` n `88`; fx avg `-0.0021` n `6`; index avg `-0.0018` n `23`; metal avg `-0.0116` n `20`; unknown avg `2.067` n `750`
- 1h: commodity avg `0.016` n `12`; crypto_alt avg `-0.2914` n `228`; crypto_major avg `-0.3411` n `8`; equity avg `-0.0069` n `88`; fx avg `0.0155` n `6`; index avg `-0.0073` n `23`; metal avg `-0.0074` n `20`; unknown avg `-0.5708` n `750`
- 4h: commodity avg `0.046` n `12`; crypto_alt avg `0.2865` n `228`; crypto_major avg `0.6197` n `8`; equity avg `0.2864` n `88`; fx avg `0.0222` n `6`; index avg `0.0522` n `23`; metal avg `0.0197` n `20`; unknown avg `-0.2201` n `724`
- 24h: commodity avg `0.193` n `12`; crypto_alt avg `-0.0663` n `228`; crypto_major avg `-0.5662` n `8`; equity avg `0.1259` n `88`; fx avg `0.0023` n `6`; index avg `-0.0573` n `23`; metal avg `-0.0137` n `20`; unknown avg `16.3618` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2187`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
