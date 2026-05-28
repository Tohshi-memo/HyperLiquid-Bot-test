# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T14:52:21.645036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0524` n `12`; crypto_alt avg `0.0636` n `228`; crypto_major avg `0.0592` n `8`; equity avg `0.3389` n `67`; fx avg `-0.0064` n `6`; index avg `0.0304` n `23`; metal avg `0.2156` n `18`; unknown avg `0.0046` n `419`
- 1h: commodity avg `-0.0512` n `12`; crypto_alt avg `-0.1595` n `228`; crypto_major avg `0.1038` n `8`; equity avg `1.1474` n `67`; fx avg `-0.0133` n `6`; index avg `0.4236` n `23`; metal avg `0.8689` n `18`; unknown avg `-0.0522` n `419`
- 4h: commodity avg `0.2221` n `12`; crypto_alt avg `-0.1109` n `228`; crypto_major avg `0.1474` n `8`; equity avg `1.5699` n `67`; fx avg `0.0848` n `6`; index avg `0.6528` n `23`; metal avg `1.2023` n `18`; unknown avg `-0.3735` n `419`
- 24h: commodity avg `0.2705` n `12`; crypto_alt avg `-5.0509` n `228`; crypto_major avg `-2.9339` n `8`; equity avg `0.4093` n `67`; fx avg `-0.0138` n `6`; index avg `0.2636` n `23`; metal avg `-0.0756` n `18`; unknown avg `-1.5996` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
