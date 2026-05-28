# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T08:22:16.167028+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.066` n `12`; crypto_alt avg `-0.3336` n `228`; crypto_major avg `-0.3377` n `8`; equity avg `0.017` n `67`; fx avg `-0.004` n `6`; index avg `0.0034` n `23`; metal avg `-0.0205` n `18`; unknown avg `-0.1091` n `419`
- 1h: commodity avg `-0.1271` n `12`; crypto_alt avg `-0.2186` n `228`; crypto_major avg `-0.2242` n `8`; equity avg `0.104` n `67`; fx avg `-0.0275` n `6`; index avg `0.0432` n `23`; metal avg `-0.0068` n `18`; unknown avg `-0.0456` n `419`
- 4h: commodity avg `-0.5752` n `12`; crypto_alt avg `0.3929` n `228`; crypto_major avg `0.5619` n `8`; equity avg `1.5985` n `67`; fx avg `0.0332` n `6`; index avg `0.5999` n `23`; metal avg `0.8143` n `18`; unknown avg `0.0071` n `409`
- 24h: commodity avg `0.4831` n `12`; crypto_alt avg `-5.2052` n `228`; crypto_major avg `-3.8314` n `8`; equity avg `-1.3328` n `67`; fx avg `-0.119` n `6`; index avg `-0.9708` n `23`; metal avg `-1.4234` n `18`; unknown avg `-1.8889` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1705`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
