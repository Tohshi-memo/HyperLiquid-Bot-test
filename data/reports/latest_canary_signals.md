# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T15:52:25.973817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `0.1559` n `231`; crypto_major avg `0.0401` n `8`; equity avg `0.0129` n `128`; fx avg `0.0007` n `6`; index avg `-0.0032` n `26`; metal avg `0.007` n `20`; unknown avg `0.225` n `790`
- 1h: commodity avg `-0.051` n `12`; crypto_alt avg `-0.11` n `231`; crypto_major avg `-0.0928` n `8`; equity avg `-0.0307` n `128`; fx avg `-0.0028` n `6`; index avg `0.002` n `26`; metal avg `0.0172` n `20`; unknown avg `0.1203` n `788`
- 4h: commodity avg `-0.0471` n `12`; crypto_alt avg `1.0369` n `231`; crypto_major avg `0.7506` n `8`; equity avg `-0.0228` n `128`; fx avg `-0.0015` n `6`; index avg `-0.0011` n `26`; metal avg `0.0545` n `20`; unknown avg `2.1305` n `772`
- 24h: commodity avg `0.035` n `12`; crypto_alt avg `-0.3059` n `231`; crypto_major avg `-0.5018` n `8`; equity avg `-0.3433` n `128`; fx avg `-0.0683` n `6`; index avg `-0.0935` n `26`; metal avg `-0.4978` n `20`; unknown avg `0.1559` n `730`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2095`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
