# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T23:37:16.760013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `12`; crypto_alt avg `0.104` n `228`; crypto_major avg `0.0136` n `8`; equity avg `-0.024` n `67`; fx avg `-0.0277` n `6`; index avg `-0.021` n `23`; metal avg `-0.524` n `18`; unknown avg `0.0439` n `405`
- 1h: commodity avg `0.1927` n `12`; crypto_alt avg `0.3184` n `228`; crypto_major avg `0.2114` n `8`; equity avg `-0.1527` n `67`; fx avg `-0.0258` n `6`; index avg `-0.1124` n `23`; metal avg `-0.3637` n `18`; unknown avg `-0.1822` n `405`
- 4h: commodity avg `0.099` n `12`; crypto_alt avg `-0.6843` n `228`; crypto_major avg `-0.3238` n `8`; equity avg `-0.2433` n `67`; fx avg `0.004` n `6`; index avg `-0.1769` n `23`; metal avg `-0.4219` n `18`; unknown avg `-0.5663` n `405`
- 24h: commodity avg `-0.2168` n `12`; crypto_alt avg `1.6051` n `228`; crypto_major avg `-0.1314` n `8`; equity avg `0.5845` n `67`; fx avg `-0.0853` n `6`; index avg `0.4137` n `23`; metal avg `-0.33` n `18`; unknown avg `0.8111` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
