# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T04:22:17.239002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `0.1009` n `228`; crypto_major avg `-0.0856` n `8`; equity avg `0.0185` n `67`; fx avg `-0.0045` n `6`; index avg `0.0092` n `23`; metal avg `-0.0323` n `18`; unknown avg `-0.2204` n `407`
- 1h: commodity avg `0.1194` n `12`; crypto_alt avg `0.2376` n `228`; crypto_major avg `0.0795` n `8`; equity avg `0.0611` n `67`; fx avg `0.0016` n `6`; index avg `0.0545` n `23`; metal avg `-0.163` n `18`; unknown avg `-0.1316` n `407`
- 4h: commodity avg `0.1037` n `12`; crypto_alt avg `-1.0612` n `228`; crypto_major avg `-0.8928` n `8`; equity avg `-0.0513` n `67`; fx avg `-0.0932` n `6`; index avg `0.0831` n `23`; metal avg `-0.2355` n `18`; unknown avg `0.3225` n `407`
- 24h: commodity avg `0.486` n `12`; crypto_alt avg `-0.1194` n `228`; crypto_major avg `-0.8879` n `8`; equity avg `-0.404` n `67`; fx avg `-0.0202` n `6`; index avg `-0.0391` n `23`; metal avg `-0.3234` n `18`; unknown avg `0.301` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1718`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
