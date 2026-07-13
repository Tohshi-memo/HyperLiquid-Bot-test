# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T19:37:26.260148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0358` n `12`; crypto_alt avg `0.1922` n `230`; crypto_major avg `0.1971` n `8`; equity avg `-0.0443` n `92`; fx avg `0.0005` n `6`; index avg `-0.0359` n `25`; metal avg `-0.0035` n `20`; unknown avg `0.0614` n `766`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `0.1663` n `230`; crypto_major avg `0.3234` n `8`; equity avg `-0.1476` n `92`; fx avg `-0.0073` n `6`; index avg `-0.0636` n `25`; metal avg `-0.0397` n `20`; unknown avg `0.088` n `766`
- 4h: commodity avg `0.6986` n `12`; crypto_alt avg `-1.0707` n `230`; crypto_major avg `-0.6729` n `8`; equity avg `-1.3649` n `92`; fx avg `-0.0029` n `6`; index avg `-0.2537` n `25`; metal avg `-0.257` n `20`; unknown avg `-0.0472` n `766`
- 24h: commodity avg `0.6794` n `12`; crypto_alt avg `-2.3248` n `230`; crypto_major avg `-2.9145` n `8`; equity avg `-3.4782` n `92`; fx avg `-0.0812` n `6`; index avg `-0.6847` n `25`; metal avg `-0.586` n `20`; unknown avg `-0.2788` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
