# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T11:37:26.394788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.7417` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6003` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1383` n `12`; crypto_alt avg `0.0363` n `228`; crypto_major avg `0.1235` n `8`; equity avg `-0.0331` n `73`; fx avg `0.0012` n `6`; index avg `-0.0972` n `23`; metal avg `0.0509` n `18`; unknown avg `-0.1683` n `424`
- 1h: commodity avg `-0.3395` n `12`; crypto_alt avg `-0.7387` n `228`; crypto_major avg `-0.6245` n `8`; equity avg `-0.205` n `73`; fx avg `0.0053` n `6`; index avg `-0.1367` n `23`; metal avg `0.2636` n `18`; unknown avg `0.6324` n `424`
- 4h: commodity avg `-0.239` n `12`; crypto_alt avg `-2.724` n `228`; crypto_major avg `-2.2361` n `8`; equity avg `-1.5041` n `73`; fx avg `0.0554` n `6`; index avg `-0.6358` n `23`; metal avg `0.5056` n `18`; unknown avg `-1.0155` n `424`
- 24h: commodity avg `-0.9803` n `12`; crypto_alt avg `-8.4529` n `228`; crypto_major avg `-7.0003` n `8`; equity avg `-5.0571` n `73`; fx avg `0.0799` n `6`; index avg `-1.7201` n `23`; metal avg `-0.7912` n `18`; unknown avg `-1.5728` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
