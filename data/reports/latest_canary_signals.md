# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T09:07:31.430942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `0.1492` n `230`; crypto_major avg `0.1176` n `8`; equity avg `0.0443` n `93`; fx avg `-0.0033` n `6`; index avg `0.0086` n `25`; metal avg `-0.0097` n `20`; unknown avg `0.0049` n `767`
- 1h: commodity avg `-0.2186` n `12`; crypto_alt avg `0.369` n `230`; crypto_major avg `0.4381` n `8`; equity avg `0.1306` n `93`; fx avg `-0.0107` n `6`; index avg `0.0246` n `25`; metal avg `0.0843` n `20`; unknown avg `0.0564` n `767`
- 4h: commodity avg `-0.1019` n `12`; crypto_alt avg `0.0816` n `230`; crypto_major avg `0.2751` n `8`; equity avg `-0.1369` n `93`; fx avg `-0.0163` n `6`; index avg `-0.0551` n `25`; metal avg `0.0529` n `20`; unknown avg `-0.0767` n `747`
- 24h: commodity avg `-0.3026` n `12`; crypto_alt avg `1.6097` n `230`; crypto_major avg `3.1971` n `8`; equity avg `1.2628` n `92`; fx avg `0.0222` n `6`; index avg `0.4312` n `25`; metal avg `0.3371` n `20`; unknown avg `0.2844` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0459`, n `668`, weak_sample_signal
