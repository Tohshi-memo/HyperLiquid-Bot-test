# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T09:52:24.725899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0509` n `12`; crypto_alt avg `-0.1496` n `228`; crypto_major avg `-0.0259` n `8`; equity avg `0.0413` n `67`; fx avg `0.0008` n `6`; index avg `0.0326` n `23`; metal avg `0.0645` n `18`; unknown avg `-0.0526` n `418`
- 1h: commodity avg `0.2138` n `12`; crypto_alt avg `-0.3068` n `228`; crypto_major avg `0.0986` n `8`; equity avg `0.1102` n `67`; fx avg `-0.0083` n `6`; index avg `-0.0929` n `23`; metal avg `0.1267` n `18`; unknown avg `-0.384` n `418`
- 4h: commodity avg `-0.6985` n `12`; crypto_alt avg `-0.1262` n `228`; crypto_major avg `0.4731` n `8`; equity avg `0.7177` n `67`; fx avg `-0.0176` n `6`; index avg `0.147` n `23`; metal avg `-0.0232` n `18`; unknown avg `-0.1001` n `400`
- 24h: commodity avg `-1.7553` n `12`; crypto_alt avg `-1.0937` n `228`; crypto_major avg `0.3833` n `8`; equity avg `0.9623` n `67`; fx avg `-0.0765` n `6`; index avg `0.8324` n `23`; metal avg `-0.1496` n `18`; unknown avg `0.9543` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
