# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T11:07:32.316594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7468` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.7178` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0241` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1013` n `12`; crypto_alt avg `0.3585` n `234`; crypto_major avg `0.4031` n `8`; equity avg `-0.0607` n `140`; fx avg `-0.0021` n `6`; index avg `-0.0083` n `26`; metal avg `-0.024` n `20`; unknown avg `13.3496` n `942`
- 1h: commodity avg `-0.0682` n `12`; crypto_alt avg `0.9198` n `234`; crypto_major avg `0.4648` n `8`; equity avg `-0.0335` n `140`; fx avg `0.0` n `6`; index avg `0.0057` n `26`; metal avg `-0.0595` n `20`; unknown avg `13.1125` n `942`
- 4h: commodity avg `-0.0972` n `12`; crypto_alt avg `2.2342` n `234`; crypto_major avg `2.6496` n `8`; equity avg `0.6255` n `140`; fx avg `-0.0295` n `6`; index avg `0.0805` n `26`; metal avg `-0.0682` n `20`; unknown avg `16.0432` n `934`
- 24h: commodity avg `-0.7286` n `12`; crypto_alt avg `7.1281` n `234`; crypto_major avg `5.884` n `8`; equity avg `2.0114` n `140`; fx avg `-0.1176` n `6`; index avg `0.3759` n `26`; metal avg `-0.0373` n `20`; unknown avg `12.6951` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
