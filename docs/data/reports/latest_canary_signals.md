# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T22:07:16.929349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.7907` n `12`; crypto_alt avg `0.712` n `228`; crypto_major avg `0.5946` n `8`; equity avg `0.0118` n `67`; fx avg `0.0164` n `6`; index avg `-0.0367` n `23`; metal avg `1.0823` n `18`; unknown avg `0.4169` n `396`
- 1h: commodity avg `-0.7391` n `12`; crypto_alt avg `-0.4442` n `228`; crypto_major avg `-0.1524` n `8`; equity avg `-0.211` n `67`; fx avg `0.0117` n `6`; index avg `-0.0027` n `23`; metal avg `0.835` n `18`; unknown avg `0.1195` n `396`
- 4h: commodity avg `-0.6526` n `12`; crypto_alt avg `-0.9391` n `228`; crypto_major avg `-0.4254` n `8`; equity avg `-0.1268` n `67`; fx avg `0.0705` n `6`; index avg `-0.1239` n `23`; metal avg `0.5956` n `18`; unknown avg `-0.4913` n `396`
- 24h: commodity avg `0.6513` n `12`; crypto_alt avg `-2.5439` n `228`; crypto_major avg `0.0017` n `8`; equity avg `0.2591` n `67`; fx avg `0.1059` n `6`; index avg `-0.1544` n `23`; metal avg `0.6752` n `18`; unknown avg `0.1184` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
