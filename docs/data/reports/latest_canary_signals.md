# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T10:22:26.239828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.0433` n `230`; crypto_major avg `0.11` n `8`; equity avg `0.0231` n `92`; fx avg `0.0009` n `6`; index avg `0.0178` n `25`; metal avg `0.0011` n `20`; unknown avg `0.0809` n `765`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `0.2537` n `230`; crypto_major avg `0.2992` n `8`; equity avg `0.0453` n `92`; fx avg `-0.0001` n `6`; index avg `0.0071` n `25`; metal avg `0.0026` n `20`; unknown avg `0.0742` n `765`
- 4h: commodity avg `0.1645` n `12`; crypto_alt avg `0.2294` n `230`; crypto_major avg `0.4073` n `8`; equity avg `0.0508` n `92`; fx avg `0.0049` n `6`; index avg `0.025` n `25`; metal avg `-0.0109` n `20`; unknown avg `3.5743` n `763`
- 24h: commodity avg `0.5227` n `12`; crypto_alt avg `-0.7335` n `230`; crypto_major avg `-0.5719` n `8`; equity avg `-0.1414` n `92`; fx avg `0.0079` n `6`; index avg `-0.1127` n `25`; metal avg `-0.1109` n `20`; unknown avg `0.1118` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
