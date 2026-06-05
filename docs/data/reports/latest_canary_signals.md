# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T23:36:27.897910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.825` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0947` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.2707` n `12`; crypto_alt avg `-0.7209` n `228`; crypto_major avg `-0.7563` n `8`; equity avg `-0.3206` n `74`; fx avg `0.0` n `6`; index avg `-0.12` n `23`; metal avg `-0.0914` n `18`; unknown avg `1.0303` n `425`
- 1h: commodity avg `0.1212` n `12`; crypto_alt avg `-1.3493` n `228`; crypto_major avg `-1.3286` n `8`; equity avg `-0.6132` n `74`; fx avg `-0.0065` n `6`; index avg `-0.2339` n `23`; metal avg `-0.1564` n `18`; unknown avg `1.3276` n `425`
- 4h: commodity avg `0.1803` n `12`; crypto_alt avg `1.4721` n `228`; crypto_major avg `1.1828` n `8`; equity avg `-0.6422` n `74`; fx avg `0.01` n `6`; index avg `-0.2808` n `23`; metal avg `-0.2214` n `18`; unknown avg `2.57` n `425`
- 24h: commodity avg `-1.4545` n `12`; crypto_alt avg `-7.2096` n `228`; crypto_major avg `-6.5157` n `8`; equity avg `-6.2439` n `74`; fx avg `-0.0492` n `6`; index avg `-4.1953` n `23`; metal avg `-4.491` n `18`; unknown avg `-0.4809` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
