# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T15:37:39.400323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `3.6206` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.5509` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.5493` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-3.0258` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-3.0165` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.9894` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0277` n `13`; crypto_alt avg `-0.4927` n `239`; crypto_major avg `-0.4138` n `8`; equity avg `-1.1201` n `166`; fx avg `0.0008` n `6`; index avg `-0.0876` n `27`; metal avg `0.1177` n `20`; unknown avg `20.6081` n `1261`
- 1h: commodity avg `-0.1661` n `13`; crypto_alt avg `-2.9356` n `239`; crypto_major avg `-3.1826` n `8`; equity avg `-2.2569` n `166`; fx avg `-0.0087` n `6`; index avg `-0.1932` n `27`; metal avg `-0.1568` n `20`; unknown avg `0.1409` n `1257`
- 4h: commodity avg `-0.2244` n `13`; crypto_alt avg `-3.6426` n `239`; crypto_major avg `-3.7753` n `8`; equity avg `-2.3315` n `166`; fx avg `0.0155` n `6`; index avg `-0.1547` n `27`; metal avg `-0.226` n `20`; unknown avg `0.3065` n `1251`
- 24h: commodity avg `-0.499` n `13`; crypto_alt avg `-6.1968` n `239`; crypto_major avg `-6.0361` n `8`; equity avg `-7.9357` n `166`; fx avg `-0.004` n `6`; index avg `-0.6508` n `27`; metal avg `-1.0847` n `20`; unknown avg `34.7238` n `1154`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
