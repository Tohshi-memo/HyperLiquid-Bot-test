# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T02:52:16.504994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0864` n `12`; crypto_alt avg `0.3205` n `228`; crypto_major avg `0.2109` n `8`; equity avg `-0.008` n `67`; fx avg `0.0027` n `6`; index avg `0.072` n `23`; metal avg `-0.0031` n `18`; unknown avg `0.8038` n `396`
- 1h: commodity avg `0.1869` n `12`; crypto_alt avg `-0.2524` n `228`; crypto_major avg `-0.1035` n `8`; equity avg `-0.0578` n `67`; fx avg `-0.0008` n `6`; index avg `0.1688` n `23`; metal avg `-0.022` n `18`; unknown avg `0.7939` n `396`
- 4h: commodity avg `0.5114` n `12`; crypto_alt avg `0.0199` n `228`; crypto_major avg `0.646` n `8`; equity avg `0.2829` n `67`; fx avg `-0.0169` n `6`; index avg `0.5882` n `23`; metal avg `0.35` n `18`; unknown avg `1.1643` n `396`
- 24h: commodity avg `-2.5439` n `12`; crypto_alt avg `1.9536` n `228`; crypto_major avg `2.3703` n `8`; equity avg `2.1487` n `67`; fx avg `0.0407` n `6`; index avg `1.2729` n `23`; metal avg `1.1218` n `18`; unknown avg `2.6642` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
