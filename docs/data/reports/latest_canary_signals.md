# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T03:52:29.471662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0053` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9184` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7635` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0133` n `13`; crypto_alt avg `0.0294` n `238`; crypto_major avg `0.0311` n `8`; equity avg `0.019` n `155`; fx avg `-0.0009` n `6`; index avg `-0.0006` n `27`; metal avg `0.0023` n `20`; unknown avg `-0.092` n `1234`
- 1h: commodity avg `-0.0365` n `13`; crypto_alt avg `-0.1676` n `238`; crypto_major avg `-0.1733` n `8`; equity avg `-0.0495` n `155`; fx avg `0.0002` n `6`; index avg `-0.0137` n `27`; metal avg `-0.1292` n `20`; unknown avg `1.1561` n `1218`
- 4h: commodity avg `-0.0196` n `13`; crypto_alt avg `-2.7213` n `238`; crypto_major avg `-2.0249` n `8`; equity avg `-0.8829` n `155`; fx avg `-0.0907` n `6`; index avg `-0.1065` n `27`; metal avg `-0.2614` n `20`; unknown avg `3.81` n `1204`
- 24h: commodity avg `-0.1166` n `13`; crypto_alt avg `-2.9162` n `238`; crypto_major avg `-2.1221` n `8`; equity avg `-1.5475` n `154`; fx avg `-0.0195` n `6`; index avg `-0.1738` n `27`; metal avg `-0.2845` n `20`; unknown avg `29.5521` n `978`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
