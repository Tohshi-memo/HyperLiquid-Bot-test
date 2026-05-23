# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T02:52:15.944747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0169` n `12`; crypto_alt avg `0.1568` n `228`; crypto_major avg `0.1657` n `8`; equity avg `0.0246` n `67`; fx avg `0.001` n `6`; index avg `0.0051` n `23`; metal avg `0.0176` n `18`; unknown avg `-0.1558` n `386`
- 1h: commodity avg `-0.2442` n `12`; crypto_alt avg `0.2649` n `228`; crypto_major avg `0.1786` n `8`; equity avg `-0.0282` n `67`; fx avg `-0.0013` n `6`; index avg `0.0037` n `23`; metal avg `0.0079` n `18`; unknown avg `-0.1744` n `386`
- 4h: commodity avg `0.3064` n `12`; crypto_alt avg `-0.2997` n `228`; crypto_major avg `-0.4009` n `8`; equity avg `-0.3392` n `67`; fx avg `-0.0067` n `6`; index avg `-0.1731` n `23`; metal avg `-0.106` n `18`; unknown avg `-1.2798` n `386`
- 24h: commodity avg `-0.0373` n `12`; crypto_alt avg `-3.4749` n `228`; crypto_major avg `-2.6112` n `8`; equity avg `-1.6923` n `67`; fx avg `0.0953` n `6`; index avg `-0.0031` n `23`; metal avg `-0.7603` n `18`; unknown avg `-2.1492` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
