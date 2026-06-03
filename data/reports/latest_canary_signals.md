# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T08:07:24.499231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.5217` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.5748` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0512` n `12`; crypto_alt avg `-0.2308` n `228`; crypto_major avg `-0.1776` n `8`; equity avg `-0.2082` n `72`; fx avg `-0.0027` n `6`; index avg `-0.0373` n `23`; metal avg `-0.0865` n `18`; unknown avg `-0.1063` n `420`
- 1h: commodity avg `0.1719` n `12`; crypto_alt avg `0.1888` n `228`; crypto_major avg `0.1558` n `8`; equity avg `-0.089` n `72`; fx avg `-0.0107` n `6`; index avg `-0.0319` n `23`; metal avg `-0.2458` n `18`; unknown avg `0.2573` n `420`
- 4h: commodity avg `0.5313` n `12`; crypto_alt avg `2.5535` n `228`; crypto_major avg `1.6484` n `8`; equity avg `0.0736` n `72`; fx avg `0.0387` n `6`; index avg `-0.0937` n `23`; metal avg `-0.8733` n `18`; unknown avg `0.6268` n `410`
- 24h: commodity avg `1.498` n `12`; crypto_alt avg `-1.1805` n `228`; crypto_major avg `-3.3142` n `8`; equity avg `0.5748` n `72`; fx avg `0.0141` n `6`; index avg `0.9348` n `23`; metal avg `-1.9883` n `18`; unknown avg `0.3854` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
