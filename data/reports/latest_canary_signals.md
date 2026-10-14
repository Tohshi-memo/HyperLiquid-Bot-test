# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T22:43:08.212286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `13`; crypto_alt avg `-0.0997` n `236`; crypto_major avg `-0.1655` n `8`; equity avg `-0.2634` n `151`; fx avg `0.016` n `6`; index avg `-0.0127` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.0328` n `1136`
- 1h: commodity avg `-0.0042` n `13`; crypto_alt avg `-0.3059` n `236`; crypto_major avg `-0.487` n `8`; equity avg `-0.8452` n `151`; fx avg `-0.0006` n `6`; index avg `-0.0979` n `26`; metal avg `0.0289` n `20`; unknown avg `-0.3123` n `1054`
- 4h: commodity avg `0.0631` n `13`; crypto_alt avg `0.3832` n `236`; crypto_major avg `0.0205` n `8`; equity avg `-1.2764` n `151`; fx avg `0.0158` n `6`; index avg `-0.138` n `26`; metal avg `0.0195` n `20`; unknown avg `0.8784` n `998`
- 24h: commodity avg `-0.1043` n `13`; crypto_alt avg `-2.3397` n `236`; crypto_major avg `-2.3024` n `8`; equity avg `-5.4249` n `151`; fx avg `-0.1435` n `6`; index avg `-0.6874` n `26`; metal avg `-0.8093` n `20`; unknown avg `1393.1432` n `890`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0875`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0855`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0801`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0536`, n `666`, weak_sample_signal
