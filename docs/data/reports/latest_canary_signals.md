# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T01:37:14.512220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1211` n `12`; crypto_alt avg `-0.4998` n `228`; crypto_major avg `-0.3622` n `8`; equity avg `-0.3133` n `67`; fx avg `-0.0204` n `6`; index avg `-0.0904` n `23`; metal avg `-0.3307` n `18`; unknown avg `1.0004` n `407`
- 1h: commodity avg `0.3018` n `12`; crypto_alt avg `-0.9826` n `228`; crypto_major avg `-0.6186` n `8`; equity avg `-0.5887` n `67`; fx avg `-0.0385` n `6`; index avg `-0.1221` n `23`; metal avg `-0.5513` n `18`; unknown avg `4.3315` n `407`
- 4h: commodity avg `0.2234` n `12`; crypto_alt avg `-2.0528` n `228`; crypto_major avg `-1.2168` n `8`; equity avg `-1.2159` n `67`; fx avg `-0.1041` n `6`; index avg `-0.5567` n `23`; metal avg `-0.9655` n `18`; unknown avg `4.1219` n `405`
- 24h: commodity avg `0.0913` n `12`; crypto_alt avg `-0.4125` n `228`; crypto_major avg `-1.2086` n `8`; equity avg `-0.4001` n `67`; fx avg `-0.0194` n `6`; index avg `-0.0043` n `23`; metal avg `-0.5029` n `18`; unknown avg `1.32` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
