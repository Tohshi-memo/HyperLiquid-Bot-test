# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T17:52:29.639806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5919` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.5915` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.4485` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.232` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0509` n `12`; crypto_alt avg `0.1986` n `234`; crypto_major avg `0.2876` n `8`; equity avg `0.1927` n `141`; fx avg `-0.0247` n `6`; index avg `0.0409` n `26`; metal avg `0.101` n `20`; unknown avg `0.6072` n `943`
- 1h: commodity avg `-0.0336` n `12`; crypto_alt avg `0.4232` n `234`; crypto_major avg `0.5677` n `8`; equity avg `0.1983` n `141`; fx avg `0.0035` n `6`; index avg `0.0436` n `26`; metal avg `0.0842` n `20`; unknown avg `0.2649` n `933`
- 4h: commodity avg `0.0436` n `12`; crypto_alt avg `-3.3639` n `234`; crypto_major avg `-2.5483` n `8`; equity avg `-0.3163` n `141`; fx avg `-0.0256` n `6`; index avg `-0.0998` n `26`; metal avg `0.0432` n `20`; unknown avg `1.664` n `907`
- 24h: commodity avg `0.4091` n `12`; crypto_alt avg `-2.4595` n `234`; crypto_major avg `-3.2671` n `8`; equity avg `-1.1945` n `140`; fx avg `0.0062` n `6`; index avg `-0.3285` n `26`; metal avg `-0.6529` n `20`; unknown avg `12.8571` n `878`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
