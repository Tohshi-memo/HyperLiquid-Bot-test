# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T01:07:15.874870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1224` n `12`; crypto_alt avg `-0.0259` n `228`; crypto_major avg `-0.0693` n `8`; equity avg `-0.0452` n `66`; fx avg `-0.0145` n `6`; index avg `-0.0302` n `23`; metal avg `-0.3351` n `18`; unknown avg `-0.1006` n `384`
- 1h: commodity avg `0.1095` n `12`; crypto_alt avg `-0.2107` n `228`; crypto_major avg `-0.1848` n `8`; equity avg `-0.0217` n `66`; fx avg `-0.0297` n `6`; index avg `-0.0317` n `23`; metal avg `-0.0027` n `18`; unknown avg `-0.2994` n `383`
- 4h: commodity avg `0.0093` n `12`; crypto_alt avg `-0.4284` n `228`; crypto_major avg `-0.5401` n `8`; equity avg `-0.3019` n `66`; fx avg `-0.0134` n `6`; index avg `-0.1021` n `23`; metal avg `0.108` n `18`; unknown avg `-0.5345` n `383`
- 24h: commodity avg `0.8092` n `12`; crypto_alt avg `-1.5252` n `228`; crypto_major avg `-1.3115` n `8`; equity avg `-0.3173` n `66`; fx avg `-0.065` n `6`; index avg `-0.6554` n `23`; metal avg `-2.617` n `18`; unknown avg `0.5441` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
