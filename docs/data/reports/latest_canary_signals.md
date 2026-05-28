# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T03:22:20.473376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2596` n `12`; crypto_alt avg `-0.7693` n `228`; crypto_major avg `-0.6169` n `8`; equity avg `-0.3162` n `67`; fx avg `-0.0154` n `6`; index avg `-0.0967` n `23`; metal avg `-0.3817` n `18`; unknown avg `-0.1665` n `419`
- 1h: commodity avg `0.6069` n `12`; crypto_alt avg `-0.779` n `228`; crypto_major avg `-0.4338` n `8`; equity avg `-0.4729` n `67`; fx avg `-0.0141` n `6`; index avg `-0.1767` n `23`; metal avg `-0.408` n `18`; unknown avg `-0.3231` n `419`
- 4h: commodity avg `0.655` n `12`; crypto_alt avg `-1.0146` n `228`; crypto_major avg `-0.7464` n `8`; equity avg `-1.0193` n `67`; fx avg `-0.0075` n `6`; index avg `-0.3631` n `23`; metal avg `-1.4503` n `18`; unknown avg `-0.5319` n `419`
- 24h: commodity avg `0.1139` n `12`; crypto_alt avg `-3.081` n `228`; crypto_major avg `-2.5746` n `8`; equity avg `-1.4191` n `67`; fx avg `-0.0592` n `6`; index avg `-1.0291` n `23`; metal avg `-2.7497` n `18`; unknown avg `-1.0969` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
