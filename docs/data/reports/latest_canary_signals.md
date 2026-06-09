# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T04:07:24.005882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8421` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5258` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0849` n `12`; crypto_alt avg `0.0318` n `228`; crypto_major avg `-0.059` n `8`; equity avg `0.0527` n `74`; fx avg `-0.0034` n `6`; index avg `0.0215` n `23`; metal avg `-0.0085` n `18`; unknown avg `-0.1396` n `517`
- 1h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.1435` n `228`; crypto_major avg `-0.3522` n `8`; equity avg `0.3831` n `74`; fx avg `-0.0013` n `6`; index avg `0.1932` n `23`; metal avg `0.0065` n `18`; unknown avg `-0.4303` n `517`
- 4h: commodity avg `-0.1544` n `12`; crypto_alt avg `-1.4567` n `228`; crypto_major avg `-1.1296` n `8`; equity avg `0.7125` n `74`; fx avg `-0.0944` n `6`; index avg `0.3962` n `23`; metal avg `0.1382` n `18`; unknown avg `-0.3776` n `517`
- 24h: commodity avg `-1.092` n `12`; crypto_alt avg `-0.8779` n `228`; crypto_major avg `-0.0083` n `8`; equity avg `1.7794` n `74`; fx avg `-0.3006` n `6`; index avg `0.8191` n `23`; metal avg `0.0289` n `18`; unknown avg `-3.1449` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
