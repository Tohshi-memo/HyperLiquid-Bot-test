# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T23:07:17.721660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2542` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.073` n `12`; crypto_alt avg `-0.0433` n `228`; crypto_major avg `-0.1872` n `8`; equity avg `0.0163` n `67`; fx avg `0.0002` n `6`; index avg `-0.0091` n `23`; metal avg `-0.0224` n `18`; unknown avg `-0.0916` n `419`
- 1h: commodity avg `0.1054` n `12`; crypto_alt avg `-0.3941` n `228`; crypto_major avg `-0.5772` n `8`; equity avg `-0.0358` n `67`; fx avg `0.0078` n `6`; index avg `-0.0831` n `23`; metal avg `-0.1143` n `18`; unknown avg `-0.1121` n `419`
- 4h: commodity avg `0.1985` n `12`; crypto_alt avg `-1.9389` n `228`; crypto_major avg `-1.2365` n `8`; equity avg `0.0026` n `67`; fx avg `-0.0073` n `6`; index avg `0.0177` n `23`; metal avg `0.0056` n `18`; unknown avg `-0.198` n `419`
- 24h: commodity avg `-1.1268` n `12`; crypto_alt avg `-2.1591` n `228`; crypto_major avg `-1.467` n `8`; equity avg `-0.2592` n `67`; fx avg `-0.0879` n `6`; index avg `-0.4917` n `23`; metal avg `-1.413` n `18`; unknown avg `-0.3069` n `400`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
