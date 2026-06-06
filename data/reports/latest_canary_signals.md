# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T07:22:22.561142+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `12`; crypto_alt avg `0.4708` n `228`; crypto_major avg `0.2835` n `8`; equity avg `-0.0496` n `74`; fx avg `0.0038` n `6`; index avg `0.0784` n `23`; metal avg `0.0363` n `18`; unknown avg `0.1679` n `425`
- 1h: commodity avg `-0.1317` n `12`; crypto_alt avg `-0.2009` n `228`; crypto_major avg `-0.5251` n `8`; equity avg `-0.4783` n `74`; fx avg `-0.011` n `6`; index avg `-0.0887` n `23`; metal avg `0.0199` n `18`; unknown avg `1.3302` n `425`
- 4h: commodity avg `-0.5153` n `12`; crypto_alt avg `-0.2563` n `228`; crypto_major avg `0.1379` n `8`; equity avg `0.0581` n `74`; fx avg `0.0028` n `6`; index avg `0.0106` n `23`; metal avg `0.0518` n `18`; unknown avg `-0.1224` n `415`
- 24h: commodity avg `-1.2136` n `12`; crypto_alt avg `-2.5139` n `228`; crypto_major avg `-1.8345` n `8`; equity avg `-6.1204` n `74`; fx avg `-0.2359` n `6`; index avg `-3.9789` n `23`; metal avg `-4.1884` n `18`; unknown avg `1.1089` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
