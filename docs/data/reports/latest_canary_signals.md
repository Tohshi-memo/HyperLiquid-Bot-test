# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T14:31:44.047114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4674` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.6858` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2729` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.7737` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.2234` n `13`; crypto_alt avg `0.5957` n `237`; crypto_major avg `0.4024` n `8`; equity avg `0.6336` n `151`; fx avg `0.0108` n `6`; index avg `0.1064` n `26`; metal avg `0.1647` n `20`; unknown avg `-0.6185` n `1199`
- 1h: commodity avg `-0.5701` n `13`; crypto_alt avg `2.6713` n `237`; crypto_major avg `2.1157` n `8`; equity avg `2.0962` n `151`; fx avg `0.0548` n `6`; index avg `0.3132` n `26`; metal avg `0.342` n `20`; unknown avg `1.3858` n `1108`
- 4h: commodity avg `-0.8223` n `13`; crypto_alt avg `3.3713` n `237`; crypto_major avg `2.6451` n `8`; equity avg `2.2178` n `151`; fx avg `0.087` n `6`; index avg `0.371` n `26`; metal avg `0.3722` n `20`; unknown avg `3.3618` n `1100`
- 24h: commodity avg `-0.4319` n `13`; crypto_alt avg `3.9154` n `237`; crypto_major avg `2.5754` n `8`; equity avg `0.3588` n `151`; fx avg `0.0634` n `6`; index avg `0.0862` n `26`; metal avg `0.2852` n `20`; unknown avg `4.499` n `1043`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
