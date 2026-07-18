# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T19:48:35.409514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.0366` n `230`; crypto_major avg `0.039` n `8`; equity avg `-0.0082` n `96`; fx avg `0.0002` n `6`; index avg `-0.006` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.0304` n `770`
- 1h: commodity avg `-0.0829` n `12`; crypto_alt avg `0.0817` n `230`; crypto_major avg `0.0792` n `8`; equity avg `-0.0043` n `96`; fx avg `0.006` n `6`; index avg `0.0034` n `25`; metal avg `0.0146` n `20`; unknown avg `-0.0311` n `770`
- 4h: commodity avg `0.2356` n `12`; crypto_alt avg `0.2195` n `230`; crypto_major avg `0.487` n `8`; equity avg `-0.028` n `96`; fx avg `-0.0669` n `6`; index avg `-0.0377` n `25`; metal avg `-0.0083` n `20`; unknown avg `0.0227` n `770`
- 24h: commodity avg `0.5005` n `12`; crypto_alt avg `-0.5775` n `230`; crypto_major avg `0.1544` n `8`; equity avg `-0.6333` n `96`; fx avg `-0.1436` n `6`; index avg `-0.0509` n `25`; metal avg `-0.012` n `20`; unknown avg `-0.0453` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
