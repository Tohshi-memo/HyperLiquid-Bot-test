# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T16:07:28.049766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7754` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2459` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0315` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0281` n `12`; crypto_alt avg `-0.0208` n `230`; crypto_major avg `0.0295` n `8`; equity avg `-0.0459` n `92`; fx avg `-0.0097` n `6`; index avg `-0.048` n `25`; metal avg `-0.0845` n `20`; unknown avg `0.0413` n `766`
- 1h: commodity avg `0.3388` n `12`; crypto_alt avg `0.0849` n `230`; crypto_major avg `0.2771` n `8`; equity avg `-0.1016` n `92`; fx avg `-0.0176` n `6`; index avg `-0.0754` n `25`; metal avg `-0.3832` n `20`; unknown avg `-0.231` n `766`
- 4h: commodity avg `-0.0938` n `12`; crypto_alt avg `1.8171` n `230`; crypto_major avg `2.6816` n `8`; equity avg `0.6501` n `92`; fx avg `-0.0309` n `6`; index avg `0.1882` n `25`; metal avg `0.4357` n `20`; unknown avg `0.7692` n `758`
- 24h: commodity avg `0.9074` n `12`; crypto_alt avg `1.1347` n `230`; crypto_major avg `2.8108` n `8`; equity avg `0.2554` n `92`; fx avg `-0.0074` n `6`; index avg `0.174` n `25`; metal avg `0.417` n `20`; unknown avg `-0.2288` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
