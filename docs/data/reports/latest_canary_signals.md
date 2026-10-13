# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T00:52:23.512022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.0204` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.8125` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.7454` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.5831` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.5754` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.5618` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0125` n `13`; crypto_alt avg `-1.7912` n `235`; crypto_major avg `-1.1183` n `8`; equity avg `-0.3745` n `151`; fx avg `0.0332` n `6`; index avg `-0.039` n `26`; metal avg `-0.0424` n `20`; unknown avg `2.067` n `1135`
- 1h: commodity avg `0.04` n `13`; crypto_alt avg `-2.6818` n `235`; crypto_major avg `-1.6976` n `8`; equity avg `-0.6982` n `151`; fx avg `0.0057` n `6`; index avg `-0.1222` n `26`; metal avg `-0.1358` n `20`; unknown avg `2.0772` n `1127`
- 4h: commodity avg `0.0766` n `13`; crypto_alt avg `-5.2432` n `235`; crypto_major avg `-3.9438` n `8`; equity avg `-1.3607` n `151`; fx avg `0.0128` n `6`; index avg `-0.1984` n `26`; metal avg `-0.1313` n `20`; unknown avg `4.3584` n `1080`
- 24h: commodity avg `0.6726` n `13`; crypto_alt avg `-7.7556` n `235`; crypto_major avg `-5.5188` n `8`; equity avg `-4.6956` n `151`; fx avg `-0.1042` n `6`; index avg `-0.5112` n `26`; metal avg `-0.364` n `20`; unknown avg `0.6171` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2068`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1849`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1194`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1031`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.095`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0861`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `666`, weak_sample_signal
