# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T09:07:25.616605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.9727` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.9178` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7908` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0569` n `12`; crypto_alt avg `0.4254` n `228`; crypto_major avg `0.4149` n `8`; equity avg `0.0956` n `74`; fx avg `-0.0061` n `6`; index avg `-0.0126` n `23`; metal avg `0.0493` n `18`; unknown avg `-0.2435` n `424`
- 1h: commodity avg `0.0913` n `12`; crypto_alt avg `-0.4959` n `228`; crypto_major avg `-0.3389` n `8`; equity avg `0.2911` n `74`; fx avg `-0.0014` n `6`; index avg `0.0677` n `23`; metal avg `0.0947` n `18`; unknown avg `-0.2923` n `424`
- 4h: commodity avg `-0.261` n `12`; crypto_alt avg `-3.1664` n `228`; crypto_major avg `-1.9924` n `8`; equity avg `-0.2016` n `74`; fx avg `0.0426` n `6`; index avg `-0.0746` n `23`; metal avg `-0.0197` n `18`; unknown avg `-0.4106` n `404`
- 24h: commodity avg `-0.2054` n `12`; crypto_alt avg `-5.3178` n `228`; crypto_major avg `-3.5128` n `8`; equity avg `-0.5165` n `73`; fx avg `0.1175` n `6`; index avg `-0.1214` n `23`; metal avg `-0.449` n `18`; unknown avg `-0.5659` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
