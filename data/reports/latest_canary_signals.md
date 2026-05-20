# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T13:07:21.477783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.055` n `12`; crypto_alt avg `0.0522` n `228`; crypto_major avg `-0.0709` n `8`; equity avg `-0.0668` n `66`; fx avg `-0.0015` n `6`; index avg `-0.008` n `23`; metal avg `-0.1768` n `18`; unknown avg `0.8308` n `384`
- 1h: commodity avg `-0.3397` n `12`; crypto_alt avg `0.437` n `228`; crypto_major avg `0.1386` n `8`; equity avg `0.0568` n `66`; fx avg `-0.0105` n `6`; index avg `0.0488` n `23`; metal avg `-0.2575` n `18`; unknown avg `1.3717` n `384`
- 4h: commodity avg `-0.2607` n `12`; crypto_alt avg `0.3759` n `228`; crypto_major avg `0.4682` n `8`; equity avg `0.3098` n `66`; fx avg `0.054` n `6`; index avg `0.131` n `23`; metal avg `-0.0992` n `18`; unknown avg `0.7758` n `384`
- 24h: commodity avg `-0.5984` n `12`; crypto_alt avg `1.2536` n `228`; crypto_major avg `0.9793` n `8`; equity avg `1.9502` n `66`; fx avg `-0.0914` n `6`; index avg `0.4384` n `23`; metal avg `-0.2837` n `18`; unknown avg `1.5869` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
