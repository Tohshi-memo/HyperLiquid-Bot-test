# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T17:52:42.131656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.3898` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.1498` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0467` n `13`; crypto_alt avg `0.1754` n `236`; crypto_major avg `0.0739` n `8`; equity avg `0.0545` n `151`; fx avg `-0.006` n `6`; index avg `0.0058` n `26`; metal avg `0.019` n `20`; unknown avg `0.5395` n `1136`
- 1h: commodity avg `0.0768` n `13`; crypto_alt avg `0.2628` n `236`; crypto_major avg `0.4752` n `8`; equity avg `0.699` n `151`; fx avg `0.0037` n `6`; index avg `0.096` n `26`; metal avg `0.0511` n `20`; unknown avg `1.0532` n `1134`
- 4h: commodity avg `0.3408` n `13`; crypto_alt avg `4.8956` n `236`; crypto_major avg `3.4906` n `8`; equity avg `2.9483` n `151`; fx avg `0.0353` n `6`; index avg `0.39` n `26`; metal avg `0.1008` n `20`; unknown avg `4.9782` n `1082`
- 24h: commodity avg `-0.1454` n `13`; crypto_alt avg `0.9258` n `236`; crypto_major avg `0.8423` n `8`; equity avg `-0.9055` n `151`; fx avg `0.2085` n `6`; index avg `-0.1428` n `26`; metal avg `0.4581` n `20`; unknown avg `0.8062` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0845`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.084`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0835`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0814`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0574`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
