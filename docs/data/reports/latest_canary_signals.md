# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T17:52:33.745263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.7239` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.4095` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.7951` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.0474` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0496` n `12`; crypto_alt avg `-0.2098` n `228`; crypto_major avg `-0.3207` n `8`; equity avg `-0.0186` n `86`; fx avg `0.0115` n `6`; index avg `0.0008` n `23`; metal avg `-0.0964` n `20`; unknown avg `-0.1479` n `764`
- 1h: commodity avg `-0.0304` n `12`; crypto_alt avg `-0.9131` n `228`; crypto_major avg `-1.0452` n `8`; equity avg `-0.8715` n `86`; fx avg `0.0074` n `6`; index avg `-0.1417` n `23`; metal avg `-0.4947` n `20`; unknown avg `-0.4252` n `764`
- 4h: commodity avg `0.1189` n `12`; crypto_alt avg `-3.6843` n `228`; crypto_major avg `-3.605` n `8`; equity avg `-1.5576` n `86`; fx avg `0.0223` n `6`; index avg `-0.1955` n `23`; metal avg `-0.8099` n `20`; unknown avg `-0.3815` n `764`
- 24h: commodity avg `-0.4268` n `12`; crypto_alt avg `-4.7129` n `228`; crypto_major avg `-4.5705` n `8`; equity avg `1.3768` n `86`; fx avg `0.0694` n `6`; index avg `-0.0842` n `23`; metal avg `-2.0682` n `20`; unknown avg `-0.1324` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
