# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T07:07:27.469573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7041` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6809` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.2518` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0547` n `12`; crypto_alt avg `-0.81` n `228`; crypto_major avg `-0.733` n `8`; equity avg `-0.0361` n `73`; fx avg `0.0248` n `6`; index avg `0.0101` n `23`; metal avg `-0.0121` n `18`; unknown avg `-0.2772` n `424`
- 1h: commodity avg `0.0002` n `12`; crypto_alt avg `-0.719` n `228`; crypto_major avg `-1.1976` n `8`; equity avg `-0.0825` n `73`; fx avg `0.0347` n `6`; index avg `0.0542` n `23`; metal avg `-0.1396` n `18`; unknown avg `-0.3889` n `424`
- 4h: commodity avg `0.0402` n `12`; crypto_alt avg `-1.6541` n `228`; crypto_major avg `-1.5673` n `8`; equity avg `0.1368` n `73`; fx avg `0.0518` n `6`; index avg `0.1136` n `23`; metal avg `-0.3267` n `18`; unknown avg `-0.2898` n `404`
- 24h: commodity avg `-0.4119` n `12`; crypto_alt avg `-4.9894` n `228`; crypto_major avg `-4.6562` n `8`; equity avg `-3.5974` n `73`; fx avg `-0.0188` n `6`; index avg `-1.0533` n `23`; metal avg `-1.3078` n `18`; unknown avg `-0.2372` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
