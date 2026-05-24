# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T12:07:15.265580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0323` n `12`; crypto_alt avg `-0.109` n `228`; crypto_major avg `-0.1208` n `8`; equity avg `-0.0308` n `67`; fx avg `-0.0011` n `6`; index avg `0.0094` n `23`; metal avg `-0.0294` n `18`; unknown avg `0.3199` n `396`
- 1h: commodity avg `-0.0217` n `12`; crypto_alt avg `-0.2181` n `228`; crypto_major avg `-0.1095` n `8`; equity avg `-0.0427` n `67`; fx avg `-0.0169` n `6`; index avg `-0.0286` n `23`; metal avg `-0.0132` n `18`; unknown avg `0.467` n `396`
- 4h: commodity avg `0.1359` n `12`; crypto_alt avg `0.1205` n `228`; crypto_major avg `0.5891` n `8`; equity avg `0.2104` n `67`; fx avg `-0.014` n `6`; index avg `-0.006` n `23`; metal avg `-0.0449` n `18`; unknown avg `0.349` n `396`
- 24h: commodity avg `-2.6021` n `12`; crypto_alt avg `3.9474` n `228`; crypto_major avg `4.7152` n `8`; equity avg `2.7486` n `67`; fx avg `0.0483` n `6`; index avg `1.2882` n `23`; metal avg `1.2951` n `18`; unknown avg `1.7573` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
