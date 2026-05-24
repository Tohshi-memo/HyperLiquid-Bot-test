# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T22:37:15.863000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0424` n `12`; crypto_alt avg `-0.1506` n `228`; crypto_major avg `-0.2282` n `8`; equity avg `0.0187` n `67`; fx avg `0.0079` n `6`; index avg `0.0477` n `23`; metal avg `0.0118` n `18`; unknown avg `-0.0901` n `396`
- 1h: commodity avg `-0.6324` n `12`; crypto_alt avg `0.8489` n `228`; crypto_major avg `0.7141` n `8`; equity avg `0.0135` n `67`; fx avg `0.0261` n `6`; index avg `0.0765` n `23`; metal avg `1.2071` n `18`; unknown avg `0.4631` n `396`
- 4h: commodity avg `-0.6056` n `12`; crypto_alt avg `-0.7143` n `228`; crypto_major avg `-0.3371` n `8`; equity avg `-0.0814` n `67`; fx avg `0.0765` n `6`; index avg `-0.0235` n `23`; metal avg `0.8019` n `18`; unknown avg `-0.4991` n `396`
- 24h: commodity avg `0.837` n `12`; crypto_alt avg `-1.5927` n `228`; crypto_major avg `0.715` n `8`; equity avg `0.4002` n `67`; fx avg `0.0881` n `6`; index avg `0.1391` n `23`; metal avg `0.8652` n `18`; unknown avg `0.3898` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
