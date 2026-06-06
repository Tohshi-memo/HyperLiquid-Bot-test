# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T10:37:24.758595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.2918` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.1225` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.018` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.7691` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6876` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6594` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.6639` n `228`; crypto_major avg `-0.6671` n `8`; equity avg `-0.0721` n `74`; fx avg `-0.0051` n `6`; index avg `0.0584` n `23`; metal avg `-0.0326` n `18`; unknown avg `-0.1539` n `425`
- 1h: commodity avg `0.0321` n `12`; crypto_alt avg `-2.4483` n `228`; crypto_major avg `-2.2597` n `8`; equity avg `-0.4906` n `74`; fx avg `0.0065` n `6`; index avg `-0.2417` n `23`; metal avg `-0.1372` n `18`; unknown avg `0.7605` n `425`
- 4h: commodity avg `0.0248` n `12`; crypto_alt avg `-1.3929` n `228`; crypto_major avg `-1.6973` n `8`; equity avg `-0.6663` n `74`; fx avg `-0.0094` n `6`; index avg `-0.0097` n `23`; metal avg `-0.0379` n `18`; unknown avg `0.9998` n `425`
- 24h: commodity avg `-1.17` n `12`; crypto_alt avg `-5.2405` n `228`; crypto_major avg `-4.6546` n `8`; equity avg `-7.315` n `74`; fx avg `-0.2717` n `6`; index avg `-4.1883` n `23`; metal avg `-4.4424` n `18`; unknown avg `1.3084` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
