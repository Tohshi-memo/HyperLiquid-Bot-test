# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T20:21:53.432746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `13`; crypto_alt avg `-0.0024` n `239`; crypto_major avg `0.0214` n `8`; equity avg `-0.0172` n `168`; fx avg `0.0` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0034` n `20`; unknown avg `0.6399` n `1268`
- 1h: commodity avg `0.0081` n `13`; crypto_alt avg `0.0776` n `239`; crypto_major avg `0.0391` n `8`; equity avg `0.0799` n `168`; fx avg `-0.0064` n `6`; index avg `0.0094` n `27`; metal avg `0.0153` n `20`; unknown avg `-0.0312` n `1244`
- 4h: commodity avg `0.099` n `13`; crypto_alt avg `0.0555` n `239`; crypto_major avg `-0.0228` n `8`; equity avg `0.2355` n `168`; fx avg `-0.0113` n `6`; index avg `0.0214` n `27`; metal avg `0.0269` n `20`; unknown avg `59.5249` n `1203`
- 24h: commodity avg `-0.0143` n `13`; crypto_alt avg `-3.0277` n `239`; crypto_major avg `-1.2586` n `8`; equity avg `-0.0239` n `168`; fx avg `-0.0081` n `6`; index avg `0.0043` n `27`; metal avg `0.0511` n `20`; unknown avg `-0.5161` n `1063`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
