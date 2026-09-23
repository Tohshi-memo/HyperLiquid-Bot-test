# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T15:52:33.705358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.1605` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.7506` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.6682` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.2679` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0471` n `12`; crypto_alt avg `-0.5643` n `234`; crypto_major avg `-0.46` n `8`; equity avg `-0.2745` n `140`; fx avg `-0.0063` n `6`; index avg `-0.0275` n `26`; metal avg `-0.0331` n `20`; unknown avg `3.4873` n `942`
- 1h: commodity avg `0.1544` n `12`; crypto_alt avg `-1.361` n `234`; crypto_major avg `-0.8395` n `8`; equity avg `-0.0904` n `140`; fx avg `0.0111` n `6`; index avg `-0.0241` n `26`; metal avg `-0.1084` n `20`; unknown avg `4.2442` n `940`
- 4h: commodity avg `0.2243` n `12`; crypto_alt avg `-4.2703` n `234`; crypto_major avg `-2.9362` n `8`; equity avg `-0.6683` n `140`; fx avg `-0.0051` n `6`; index avg `-0.1856` n `26`; metal avg `-0.268` n `20`; unknown avg `510.7897` n `898`
- 24h: commodity avg `0.4274` n `12`; crypto_alt avg `-2.3264` n `234`; crypto_major avg `-3.3442` n `8`; equity avg `-0.8054` n `140`; fx avg `0.019` n `6`; index avg `-0.2335` n `26`; metal avg `-0.5383` n `20`; unknown avg `16.0018` n `838`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2524`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
