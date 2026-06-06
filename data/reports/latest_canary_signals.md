# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T11:37:23.440140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `0.2966` n `228`; crypto_major avg `0.2599` n `8`; equity avg `0.0901` n `74`; fx avg `0.0071` n `6`; index avg `0.0165` n `23`; metal avg `0.0158` n `18`; unknown avg `-0.0098` n `425`
- 1h: commodity avg `0.0959` n `12`; crypto_alt avg `1.1142` n `228`; crypto_major avg `0.9951` n `8`; equity avg `0.4534` n `74`; fx avg `0.0086` n `6`; index avg `0.029` n `23`; metal avg `0.0564` n `18`; unknown avg `0.3784` n `425`
- 4h: commodity avg `0.1798` n `12`; crypto_alt avg `-0.1553` n `228`; crypto_major avg `-0.5249` n `8`; equity avg `0.1984` n `74`; fx avg `0.0109` n `6`; index avg `0.0375` n `23`; metal avg `-0.0426` n `18`; unknown avg `0.2212` n `425`
- 24h: commodity avg `-1.107` n `12`; crypto_alt avg `-3.6729` n `228`; crypto_major avg `-3.6298` n `8`; equity avg `-6.7081` n `74`; fx avg `-0.2796` n `6`; index avg `-4.1027` n `23`; metal avg `-4.4266` n `18`; unknown avg `1.67` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
