# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T03:22:23.349802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1634` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `-0.0762` n `228`; crypto_major avg `-0.0311` n `8`; equity avg `0.0612` n `74`; fx avg `-0.0003` n `6`; index avg `0.0286` n `23`; metal avg `-0.1411` n `18`; unknown avg `-0.3003` n `517`
- 1h: commodity avg `-0.1805` n `12`; crypto_alt avg `0.0146` n `228`; crypto_major avg `0.3548` n `8`; equity avg `0.2575` n `74`; fx avg `0.012` n `6`; index avg `0.1067` n `23`; metal avg `-0.0629` n `18`; unknown avg `-0.2801` n `517`
- 4h: commodity avg `-0.2467` n `12`; crypto_alt avg `-1.9354` n `228`; crypto_major avg `-1.1478` n `8`; equity avg `0.0982` n `74`; fx avg `-0.0618` n `6`; index avg `0.0156` n `23`; metal avg `-0.239` n `18`; unknown avg `-0.2628` n `517`
- 24h: commodity avg `-1.1227` n `12`; crypto_alt avg `-1.2316` n `228`; crypto_major avg `-0.4874` n `8`; equity avg `1.2506` n `74`; fx avg `-0.2991` n `6`; index avg `0.5188` n `23`; metal avg `0.0647` n `18`; unknown avg `-3.3019` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
