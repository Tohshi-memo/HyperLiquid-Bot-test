# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T00:37:23.129074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0862` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `-1.1897` n `228`; crypto_major avg `-0.8599` n `8`; equity avg `-0.1924` n `74`; fx avg `-0.1063` n `6`; index avg `-0.0204` n `23`; metal avg `-0.0927` n `18`; unknown avg `-0.0153` n `517`
- 1h: commodity avg `-0.0693` n `12`; crypto_alt avg `-1.4966` n `228`; crypto_major avg `-1.2844` n `8`; equity avg `-0.5968` n `74`; fx avg `-0.0553` n `6`; index avg `-0.3812` n `23`; metal avg `-0.3068` n `18`; unknown avg `-0.1141` n `517`
- 4h: commodity avg `-0.061` n `12`; crypto_alt avg `-2.2866` n `228`; crypto_major avg `-1.4079` n `8`; equity avg `-0.5482` n `74`; fx avg `-0.0613` n `6`; index avg `-0.3217` n `23`; metal avg `-0.3458` n `18`; unknown avg `-0.8473` n `517`
- 24h: commodity avg `-0.657` n `12`; crypto_alt avg `-1.7514` n `228`; crypto_major avg `-1.1183` n `8`; equity avg `0.1299` n `74`; fx avg `-0.3277` n `6`; index avg `-0.0275` n `23`; metal avg `-0.9169` n `18`; unknown avg `-3.4264` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
