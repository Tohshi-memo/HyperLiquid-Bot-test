# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T10:52:24.561244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0326` n `12`; crypto_alt avg `0.0529` n `230`; crypto_major avg `0.0227` n `8`; equity avg `-0.0018` n `100`; fx avg `0.0025` n `6`; index avg `0.0069` n `25`; metal avg `0.0105` n `20`; unknown avg `0.0587` n `775`
- 1h: commodity avg `0.1765` n `12`; crypto_alt avg `0.0764` n `230`; crypto_major avg `0.1085` n `8`; equity avg `-0.0982` n `100`; fx avg `-0.0055` n `6`; index avg `-0.0142` n `25`; metal avg `0.0221` n `20`; unknown avg `-0.0224` n `775`
- 4h: commodity avg `-0.1266` n `12`; crypto_alt avg `-0.234` n `230`; crypto_major avg `-0.1187` n `8`; equity avg `0.1764` n `100`; fx avg `-0.0599` n `6`; index avg `0.0408` n `25`; metal avg `0.1103` n `20`; unknown avg `-0.1061` n `775`
- 24h: commodity avg `-0.6417` n `12`; crypto_alt avg `0.6533` n `230`; crypto_major avg `1.3655` n `8`; equity avg `1.3094` n `100`; fx avg `0.0927` n `6`; index avg `0.1549` n `25`; metal avg `0.4077` n `20`; unknown avg `-0.1368` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
