# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T09:52:28.136643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0409` n `12`; crypto_alt avg `-0.0291` n `228`; crypto_major avg `-0.0396` n `8`; equity avg `-0.0682` n `88`; fx avg `0.0133` n `6`; index avg `-0.0121` n `23`; metal avg `-0.1307` n `20`; unknown avg `-0.1843` n `764`
- 1h: commodity avg `0.1339` n `12`; crypto_alt avg `-0.0061` n `228`; crypto_major avg `-0.1043` n `8`; equity avg `-0.1121` n `88`; fx avg `0.0158` n `6`; index avg `-0.0329` n `23`; metal avg `-0.2586` n `20`; unknown avg `-0.3555` n `764`
- 4h: commodity avg `0.1167` n `12`; crypto_alt avg `0.2298` n `228`; crypto_major avg `0.1115` n `8`; equity avg `0.2599` n `88`; fx avg `0.0635` n `6`; index avg `0.0035` n `23`; metal avg `-0.2779` n `20`; unknown avg `0.1674` n `732`
- 24h: commodity avg `-0.3121` n `12`; crypto_alt avg `0.0853` n `228`; crypto_major avg `-0.3088` n `8`; equity avg `0.3149` n `88`; fx avg `0.0592` n `6`; index avg `0.0549` n `23`; metal avg `-0.516` n `20`; unknown avg `0.257` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
