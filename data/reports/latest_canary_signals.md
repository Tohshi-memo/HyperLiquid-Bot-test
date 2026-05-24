# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T17:07:23.296831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `12`; crypto_alt avg `0.1712` n `228`; crypto_major avg `0.0806` n `8`; equity avg `0.0106` n `67`; fx avg `-0.0083` n `6`; index avg `-0.0178` n `23`; metal avg `-0.0052` n `18`; unknown avg `0.0364` n `396`
- 1h: commodity avg `0.2005` n `12`; crypto_alt avg `0.0362` n `228`; crypto_major avg `0.0242` n `8`; equity avg `0.0882` n `67`; fx avg `-0.0003` n `6`; index avg `-0.0058` n `23`; metal avg `-0.0042` n `18`; unknown avg `0.0377` n `396`
- 4h: commodity avg `0.7398` n `12`; crypto_alt avg `-0.4241` n `228`; crypto_major avg `-0.7179` n `8`; equity avg `-0.3769` n `67`; fx avg `0.0142` n `6`; index avg `-0.3165` n `23`; metal avg `-0.3164` n `18`; unknown avg `-0.0986` n `396`
- 24h: commodity avg `-1.2748` n `12`; crypto_alt avg `0.5224` n `228`; crypto_major avg `2.3387` n `8`; equity avg `1.7158` n `67`; fx avg `0.0913` n `6`; index avg `0.5481` n `23`; metal avg `0.6178` n `18`; unknown avg `1.3451` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
