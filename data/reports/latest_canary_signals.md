# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T16:32:16.895733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.267` n `12`; crypto_alt avg `-0.2233` n `228`; crypto_major avg `-0.1798` n `8`; equity avg `0.0172` n `67`; fx avg `-0.0085` n `6`; index avg `-0.0038` n `23`; metal avg `0.0004` n `18`; unknown avg `-0.0364` n `396`
- 1h: commodity avg `0.118` n `12`; crypto_alt avg `0.0765` n `228`; crypto_major avg `0.0125` n `8`; equity avg `0.0404` n `67`; fx avg `0.0051` n `6`; index avg `0.0215` n `23`; metal avg `0.0981` n `18`; unknown avg `-0.2918` n `396`
- 4h: commodity avg `0.7318` n `12`; crypto_alt avg `-0.443` n `228`; crypto_major avg `-0.5537` n `8`; equity avg `-0.3812` n `67`; fx avg `0.0251` n `6`; index avg `-0.3568` n `23`; metal avg `-0.3671` n `18`; unknown avg `0.2797` n `396`
- 24h: commodity avg `-1.203` n `12`; crypto_alt avg `0.5452` n `228`; crypto_major avg `2.3172` n `8`; equity avg `1.5913` n `67`; fx avg `0.076` n `6`; index avg `0.5913` n `23`; metal avg `0.6877` n `18`; unknown avg `0.9198` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
