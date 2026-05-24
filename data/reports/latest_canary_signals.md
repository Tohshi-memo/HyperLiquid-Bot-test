# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T22:22:16.127269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0366` n `12`; crypto_alt avg `0.3012` n `228`; crypto_major avg `0.3186` n `8`; equity avg `0.02` n `67`; fx avg `-0.0005` n `6`; index avg `0.0423` n `23`; metal avg `0.1803` n `18`; unknown avg `0.1142` n `396`
- 1h: commodity avg `-0.6448` n `12`; crypto_alt avg `-0.1009` n `228`; crypto_major avg `0.2038` n `8`; equity avg `-0.1973` n `67`; fx avg `0.0073` n `6`; index avg `0.0366` n `23`; metal avg `1.0835` n `18`; unknown avg `0.4288` n `396`
- 4h: commodity avg `-0.6672` n `12`; crypto_alt avg `-0.705` n `228`; crypto_major avg `-0.1422` n `8`; equity avg `-0.1235` n `67`; fx avg `0.07` n `6`; index avg `-0.0778` n `23`; metal avg `0.793` n `18`; unknown avg `-0.4732` n `396`
- 24h: commodity avg `0.6451` n `12`; crypto_alt avg `-2.0584` n `228`; crypto_major avg `0.5527` n `8`; equity avg `0.3051` n `67`; fx avg `0.0796` n `6`; index avg `-0.0416` n `23`; metal avg `0.8707` n `18`; unknown avg `0.2163` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
