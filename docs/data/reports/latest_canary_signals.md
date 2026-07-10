# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T17:52:48.936835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0205` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.088` n `12`; crypto_alt avg `-0.0214` n `229`; crypto_major avg `0.0439` n `8`; equity avg `0.087` n `92`; fx avg `0.0042` n `6`; index avg `0.009` n `25`; metal avg `-0.0055` n `20`; unknown avg `-0.0135` n `765`
- 1h: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.1052` n `229`; crypto_major avg `-0.2031` n `8`; equity avg `-0.0092` n `92`; fx avg `-0.0163` n `6`; index avg `0.0203` n `25`; metal avg `-0.0211` n `20`; unknown avg `-0.0384` n `765`
- 4h: commodity avg `-0.0291` n `12`; crypto_alt avg `-0.5152` n `229`; crypto_major avg `-0.9328` n `8`; equity avg `-0.0558` n `92`; fx avg `-0.0332` n `6`; index avg `0.0877` n `25`; metal avg `-0.0427` n `20`; unknown avg `0.0894` n `765`
- 24h: commodity avg `-0.2823` n `12`; crypto_alt avg `0.6883` n `229`; crypto_major avg `0.8385` n `8`; equity avg `-0.8243` n `92`; fx avg `-0.1763` n `6`; index avg `0.0272` n `25`; metal avg `-0.2245` n `20`; unknown avg `-0.2033` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
