# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T14:37:29.922068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5312` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.1553` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1041` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.0288` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-1.915` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.8332` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `0.85` n `234`; crypto_major avg `0.6862` n `8`; equity avg `0.3792` n `140`; fx avg `-0.0104` n `6`; index avg `0.0374` n `26`; metal avg `0.0415` n `20`; unknown avg `0.3637` n `944`
- 1h: commodity avg `0.0514` n `12`; crypto_alt avg `-2.4104` n `234`; crypto_major avg `-1.9774` n `8`; equity avg `-0.5146` n `140`; fx avg `0.0142` n `6`; index avg `-0.1442` n `26`; metal avg `-0.0624` n `20`; unknown avg `3.6978` n `902`
- 4h: commodity avg `0.1475` n `12`; crypto_alt avg `-3.2668` n `234`; crypto_major avg `-2.3837` n `8`; equity avg `-1.1584` n `140`; fx avg `0.0133` n `6`; index avg `-0.2284` n `26`; metal avg `-0.2796` n `20`; unknown avg `517.9004` n `898`
- 24h: commodity avg `0.3693` n `12`; crypto_alt avg `0.4751` n `234`; crypto_major avg `-1.5243` n `8`; equity avg `-1.1654` n `140`; fx avg `0.0362` n `6`; index avg `-0.2965` n `26`; metal avg `-0.5183` n `20`; unknown avg `20.2994` n `830`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
