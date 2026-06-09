# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T01:07:26.786589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0747` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.0451` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.9021` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6838` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0616` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0805` n `12`; crypto_alt avg `0.3149` n `228`; crypto_major avg `0.0869` n `8`; equity avg `0.019` n `74`; fx avg `-0.0176` n `6`; index avg `0.0144` n `23`; metal avg `0.2227` n `18`; unknown avg `0.0182` n `517`
- 1h: commodity avg `-0.0033` n `12`; crypto_alt avg `-1.1369` n `228`; crypto_major avg `-1.1994` n `8`; equity avg `-0.2661` n `74`; fx avg `-0.0993` n `6`; index avg `-0.1378` n `23`; metal avg `0.0282` n `18`; unknown avg `-0.0404` n `517`
- 4h: commodity avg `-0.2619` n `12`; crypto_alt avg `-2.8618` n `228`; crypto_major avg `-2.3366` n `8`; equity avg `-0.6528` n `74`; fx avg `-0.1162` n `6`; index avg `-0.4345` n `23`; metal avg `-0.2915` n `18`; unknown avg `-0.3527` n `517`
- 24h: commodity avg `-0.4155` n `12`; crypto_alt avg `-1.175` n `228`; crypto_major avg `-0.5621` n `8`; equity avg `0.7874` n `74`; fx avg `-0.3063` n `6`; index avg `0.3036` n `23`; metal avg `-0.2076` n `18`; unknown avg `-3.2063` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
