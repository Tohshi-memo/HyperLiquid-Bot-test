# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T22:49:25.698035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0784` n `12`; crypto_alt avg `-0.1974` n `228`; crypto_major avg `-0.2583` n `8`; equity avg `-0.0217` n `67`; fx avg `-0.0019` n `6`; index avg `-0.024` n `23`; metal avg `-0.0673` n `18`; unknown avg `-0.1358` n `419`
- 1h: commodity avg `-0.0673` n `12`; crypto_alt avg `0.1408` n `228`; crypto_major avg `0.0237` n `8`; equity avg `-0.1283` n `67`; fx avg `-0.0211` n `6`; index avg `-0.0637` n `23`; metal avg `0.0816` n `18`; unknown avg `0.1196` n `419`
- 4h: commodity avg `0.1326` n `12`; crypto_alt avg `-1.6809` n `228`; crypto_major avg `-0.9231` n `8`; equity avg `-0.1555` n `67`; fx avg `-0.0161` n `6`; index avg `-0.0169` n `23`; metal avg `0.0654` n `18`; unknown avg `-0.0419` n `419`
- 24h: commodity avg `-1.187` n `12`; crypto_alt avg `-1.8896` n `228`; crypto_major avg `-1.0582` n `8`; equity avg `-0.3326` n `67`; fx avg `-0.1143` n `6`; index avg `-0.4646` n `23`; metal avg `-1.3133` n `18`; unknown avg `-0.2229` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
