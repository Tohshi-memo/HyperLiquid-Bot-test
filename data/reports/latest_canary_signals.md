# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T13:22:19.386917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1026` n `12`; crypto_alt avg `-0.0275` n `228`; crypto_major avg `-0.0247` n `8`; equity avg `-0.0232` n `67`; fx avg `0.0021` n `6`; index avg `-0.0249` n `23`; metal avg `-0.1239` n `18`; unknown avg `0.0379` n `405`
- 1h: commodity avg `0.5199` n `12`; crypto_alt avg `0.1606` n `228`; crypto_major avg `-0.0036` n `8`; equity avg `-0.0804` n `67`; fx avg `0.0014` n `6`; index avg `-0.0078` n `23`; metal avg `-0.0292` n `18`; unknown avg `-0.0022` n `405`
- 4h: commodity avg `0.5168` n `12`; crypto_alt avg `0.2256` n `228`; crypto_major avg `0.0349` n `8`; equity avg `0.0799` n `67`; fx avg `0.0202` n `6`; index avg `0.0631` n `23`; metal avg `-0.0505` n `18`; unknown avg `-0.3144` n `397`
- 24h: commodity avg `0.3476` n `12`; crypto_alt avg `0.7732` n `228`; crypto_major avg `-0.192` n `8`; equity avg `0.3693` n `67`; fx avg `0.0221` n `6`; index avg `0.1071` n `23`; metal avg `0.4979` n `18`; unknown avg `0.0545` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
