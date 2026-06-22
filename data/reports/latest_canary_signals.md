# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T00:20:56.656103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `12`; crypto_alt avg `0.0988` n `228`; crypto_major avg `0.0935` n `8`; equity avg `-0.1242` n `78`; fx avg `-0.008` n `6`; index avg `-0.0309` n `23`; metal avg `0.1997` n `18`; unknown avg `-0.4546` n `702`
- 1h: commodity avg `-0.0376` n `12`; crypto_alt avg `-0.01` n `228`; crypto_major avg `-0.0989` n `8`; equity avg `-0.529` n `78`; fx avg `0.0246` n `6`; index avg `-0.0526` n `23`; metal avg `0.0884` n `18`; unknown avg `1.6707` n `702`
- 4h: commodity avg `-0.1325` n `12`; crypto_alt avg `-1.1273` n `228`; crypto_major avg `-0.9657` n `8`; equity avg `-1.0282` n `78`; fx avg `0.0141` n `6`; index avg `-0.1798` n `23`; metal avg `0.1201` n `18`; unknown avg `0.5268` n `702`
- 24h: commodity avg `0.068` n `12`; crypto_alt avg `-0.6184` n `228`; crypto_major avg `-1.4043` n `8`; equity avg `-0.9232` n `78`; fx avg `-0.0984` n `6`; index avg `-0.1639` n `23`; metal avg `0.0163` n `18`; unknown avg `1.0514` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
