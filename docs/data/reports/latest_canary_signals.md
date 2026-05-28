# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T16:52:22.338247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3642` n `12`; crypto_alt avg `0.4262` n `228`; crypto_major avg `0.3331` n `8`; equity avg `0.0237` n `67`; fx avg `-0.0036` n `6`; index avg `0.0984` n `23`; metal avg `0.1516` n `18`; unknown avg `0.0546` n `419`
- 1h: commodity avg `-0.638` n `12`; crypto_alt avg `1.1235` n `228`; crypto_major avg `1.0273` n `8`; equity avg `0.2212` n `67`; fx avg `-0.0141` n `6`; index avg `0.2847` n `23`; metal avg `0.5623` n `18`; unknown avg `0.2286` n `419`
- 4h: commodity avg `0.1056` n `12`; crypto_alt avg `0.906` n `228`; crypto_major avg `1.2528` n `8`; equity avg `1.5764` n `67`; fx avg `-0.0171` n `6`; index avg `1.2394` n `23`; metal avg `1.6573` n `18`; unknown avg `-0.028` n `419`
- 24h: commodity avg `0.1768` n `12`; crypto_alt avg `-4.4922` n `228`; crypto_major avg `-1.9381` n `8`; equity avg `1.1921` n `67`; fx avg `-0.0015` n `6`; index avg `1.0575` n `23`; metal avg `0.6423` n `18`; unknown avg `-1.1766` n `408`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
