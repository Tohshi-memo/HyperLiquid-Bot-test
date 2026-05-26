# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T06:07:17.144023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0537` n `12`; crypto_alt avg `0.0849` n `228`; crypto_major avg `0.0508` n `8`; equity avg `0.0659` n `67`; fx avg `-0.0032` n `6`; index avg `0.026` n `23`; metal avg `0.0884` n `18`; unknown avg `0.0215` n `397`
- 1h: commodity avg `-0.1732` n `12`; crypto_alt avg `0.4233` n `228`; crypto_major avg `0.3483` n `8`; equity avg `0.1198` n `67`; fx avg `-0.027` n `6`; index avg `-0.0233` n `23`; metal avg `0.0255` n `18`; unknown avg `0.1442` n `397`
- 4h: commodity avg `0.0004` n `12`; crypto_alt avg `0.9837` n `228`; crypto_major avg `0.6355` n `8`; equity avg `0.1257` n `67`; fx avg `-0.0333` n `6`; index avg `0.0122` n `23`; metal avg `-0.0879` n `18`; unknown avg `0.2208` n `397`
- 24h: commodity avg `0.4269` n `12`; crypto_alt avg `-0.4798` n `228`; crypto_major avg `-1.1077` n `8`; equity avg `-0.4811` n `67`; fx avg `-0.0685` n `6`; index avg `-0.0229` n `23`; metal avg `-0.1852` n `18`; unknown avg `0.3684` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1824`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
