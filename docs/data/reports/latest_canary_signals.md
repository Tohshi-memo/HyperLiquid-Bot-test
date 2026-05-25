# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T10:52:18.081655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0506` n `12`; crypto_alt avg `-0.0045` n `228`; crypto_major avg `0.0091` n `8`; equity avg `0.014` n `67`; fx avg `0.0006` n `6`; index avg `0.0131` n `23`; metal avg `-0.0453` n `18`; unknown avg `0.0005` n `397`
- 1h: commodity avg `-0.0514` n `12`; crypto_alt avg `0.3122` n `228`; crypto_major avg `-0.007` n `8`; equity avg `0.0354` n `67`; fx avg `0.0043` n `6`; index avg `0.0321` n `23`; metal avg `0.1014` n `18`; unknown avg `-0.0426` n `397`
- 4h: commodity avg `-0.1621` n `12`; crypto_alt avg `0.5816` n `228`; crypto_major avg `0.3421` n `8`; equity avg `0.3104` n `67`; fx avg `0.0146` n `6`; index avg `0.0519` n `23`; metal avg `0.4056` n `18`; unknown avg `0.0331` n `397`
- 24h: commodity avg `-0.1837` n `12`; crypto_alt avg `0.7141` n `228`; crypto_major avg `0.0973` n `8`; equity avg `0.6015` n `67`; fx avg `0.0014` n `6`; index avg `-0.0058` n `23`; metal avg `0.7242` n `18`; unknown avg `0.9043` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
