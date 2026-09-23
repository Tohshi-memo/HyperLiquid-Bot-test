# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T17:07:30.964170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8827` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5842` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.583` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8439` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0544` n `12`; crypto_alt avg `-0.3328` n `234`; crypto_major avg `-0.1953` n `8`; equity avg `-0.1734` n `141`; fx avg `0.0003` n `6`; index avg `-0.0206` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.0816` n `941`
- 1h: commodity avg `-0.115` n `12`; crypto_alt avg `-0.5027` n `234`; crypto_major avg `-0.8482` n `8`; equity avg `-0.4075` n `141`; fx avg `-0.0179` n `6`; index avg `-0.0751` n `26`; metal avg `-0.0388` n `20`; unknown avg `-0.144` n `941`
- 4h: commodity avg `0.0477` n `12`; crypto_alt avg `-3.9502` n `234`; crypto_major avg `-2.835` n `8`; equity avg `-0.9911` n `141`; fx avg `-0.0339` n `6`; index avg `-0.2508` n `26`; metal avg `-0.252` n `20`; unknown avg `512.1142` n `891`
- 24h: commodity avg `0.254` n `12`; crypto_alt avg `-2.8539` n `234`; crypto_major avg `-3.7338` n `8`; equity avg `-1.4122` n `140`; fx avg `0.0042` n `6`; index avg `-0.3557` n `26`; metal avg `-0.6677` n `20`; unknown avg `13.3134` n `878`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.269`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
