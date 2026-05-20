# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T13:22:21.239034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0275` n `12`; crypto_alt avg `-0.1737` n `228`; crypto_major avg `0.1363` n `8`; equity avg `0.016` n `66`; fx avg `0.0019` n `6`; index avg `-0.0429` n `23`; metal avg `-0.0173` n `18`; unknown avg `-0.0923` n `384`
- 1h: commodity avg `-0.2101` n `12`; crypto_alt avg `0.3663` n `228`; crypto_major avg `0.4325` n `8`; equity avg `0.0373` n `66`; fx avg `-0.0057` n `6`; index avg `-0.024` n `23`; metal avg `-0.1125` n `18`; unknown avg `1.2169` n `384`
- 4h: commodity avg `-0.4399` n `12`; crypto_alt avg `0.0758` n `228`; crypto_major avg `0.4722` n `8`; equity avg `0.3419` n `66`; fx avg `0.0386` n `6`; index avg `0.1027` n `23`; metal avg `-0.0506` n `18`; unknown avg `2.3213` n `384`
- 24h: commodity avg `-0.7822` n `12`; crypto_alt avg `0.951` n `228`; crypto_major avg `1.0909` n `8`; equity avg `2.0014` n `66`; fx avg `-0.0797` n `6`; index avg `0.3767` n `23`; metal avg `-0.1797` n `18`; unknown avg `1.5203` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
