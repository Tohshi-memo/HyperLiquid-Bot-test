# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T03:22:21.362072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `0.1339` n `228`; crypto_major avg `0.2036` n `8`; equity avg `0.0819` n `66`; fx avg `-0.0099` n `6`; index avg `0.063` n `23`; metal avg `0.0454` n `18`; unknown avg `-0.3247` n `384`
- 1h: commodity avg `0.1702` n `12`; crypto_alt avg `0.0042` n `228`; crypto_major avg `0.1473` n `8`; equity avg `0.0121` n `66`; fx avg `0.0184` n `6`; index avg `0.0431` n `23`; metal avg `-0.4353` n `18`; unknown avg `0.137` n `384`
- 4h: commodity avg `0.1257` n `12`; crypto_alt avg `1.2592` n `228`; crypto_major avg `1.3735` n `8`; equity avg `0.8038` n `66`; fx avg `0.094` n `6`; index avg `0.424` n `23`; metal avg `-0.0973` n `18`; unknown avg `3.9396` n `384`
- 24h: commodity avg `-2.1758` n `12`; crypto_alt avg `3.8513` n `228`; crypto_major avg `3.8691` n `8`; equity avg `2.635` n `66`; fx avg `0.0494` n `6`; index avg `1.8023` n `23`; metal avg `1.6104` n `18`; unknown avg `5.8091` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
