# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T16:37:29.740150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0128` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.9487` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.4326` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0894` n `12`; crypto_alt avg `-0.5633` n `228`; crypto_major avg `-0.4677` n `8`; equity avg `-0.3578` n `86`; fx avg `0.0004` n `6`; index avg `-0.0576` n `23`; metal avg `-0.1563` n `20`; unknown avg `-0.0848` n `765`
- 1h: commodity avg `-0.0328` n `12`; crypto_alt avg `0.1759` n `228`; crypto_major avg `0.2663` n `8`; equity avg `0.0421` n `86`; fx avg `0.0251` n `6`; index avg `0.03` n `23`; metal avg `0.001` n `20`; unknown avg `-0.0534` n `765`
- 4h: commodity avg `0.3103` n `12`; crypto_alt avg `-2.1381` n `228`; crypto_major avg `-2.7025` n `8`; equity avg `-2.5818` n `86`; fx avg `0.0741` n `6`; index avg `-0.2699` n `23`; metal avg `0.2462` n `20`; unknown avg `1.0671` n `765`
- 24h: commodity avg `0.2303` n `12`; crypto_alt avg `-1.3675` n `228`; crypto_major avg `-1.2301` n `8`; equity avg `-0.5624` n `86`; fx avg `0.0775` n `6`; index avg `0.3206` n `23`; metal avg `0.1228` n `20`; unknown avg `0.1169` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
