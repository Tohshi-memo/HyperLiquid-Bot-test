# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T21:21:47.158327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0317` n `12`; crypto_alt avg `-0.1328` n `228`; crypto_major avg `-0.0586` n `8`; equity avg `0.0071` n `67`; fx avg `-0.0193` n `6`; index avg `-0.0019` n `23`; metal avg `-0.0067` n `18`; unknown avg `-0.1151` n `405`
- 1h: commodity avg `0.1885` n `12`; crypto_alt avg `-0.6746` n `228`; crypto_major avg `-0.2355` n `8`; equity avg `-0.056` n `67`; fx avg `0.0259` n `6`; index avg `-0.0331` n `23`; metal avg `0.0089` n `18`; unknown avg `-0.3844` n `405`
- 4h: commodity avg `0.1688` n `12`; crypto_alt avg `-0.8783` n `228`; crypto_major avg `-0.5246` n `8`; equity avg `0.0112` n `67`; fx avg `0.0508` n `6`; index avg `-0.1478` n `23`; metal avg `-0.1113` n `18`; unknown avg `-0.5331` n `405`
- 24h: commodity avg `-1.1337` n `12`; crypto_alt avg `1.9322` n `228`; crypto_major avg `0.3873` n `8`; equity avg `0.7699` n `67`; fx avg `-0.0338` n `6`; index avg `0.696` n `23`; metal avg `1.8858` n `18`; unknown avg `1.1796` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
