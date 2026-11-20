# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T15:22:35.625856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `3.3423` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.2519` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.0452` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.8695` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.7566` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.6784` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.2072` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1113` n `13`; crypto_alt avg `-2.0994` n `239`; crypto_major avg `-2.0721` n `8`; equity avg `-1.61` n `165`; fx avg `0.0108` n `6`; index avg `-0.1649` n `27`; metal avg `-0.2882` n `20`; unknown avg `-0.7359` n `1260`
- 1h: commodity avg `-0.2249` n `13`; crypto_alt avg `-2.5615` n `239`; crypto_major avg `-2.9815` n `8`; equity avg `-1.5266` n `165`; fx avg `-0.0043` n `6`; index avg `-0.112` n `27`; metal avg `-0.3031` n `20`; unknown avg `236.0978` n `1258`
- 4h: commodity avg `-0.1428` n `13`; crypto_alt avg `-3.2274` n `239`; crypto_major avg `-3.3947` n `8`; equity avg `-1.1875` n `165`; fx avg `0.0282` n `6`; index avg `-0.0524` n `27`; metal avg `-0.3495` n `20`; unknown avg `320.3198` n `1254`
- 24h: commodity avg `-0.5633` n `13`; crypto_alt avg `-6.1464` n `239`; crypto_major avg `-6.1361` n `8`; equity avg `-8.0018` n `165`; fx avg `0.0062` n `6`; index avg `-0.701` n `27`; metal avg `-1.2943` n `20`; unknown avg `37.4956` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
