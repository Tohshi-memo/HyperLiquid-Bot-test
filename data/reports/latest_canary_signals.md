# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T20:37:39.112032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.1492` n `230`; crypto_major avg `-0.2277` n `8`; equity avg `-0.0057` n `96`; fx avg `-0.0029` n `6`; index avg `0.0008` n `25`; metal avg `0.0021` n `20`; unknown avg `0.0147` n `770`
- 1h: commodity avg `-0.0609` n `12`; crypto_alt avg `0.083` n `230`; crypto_major avg `0.0499` n `8`; equity avg `-0.0256` n `96`; fx avg `0.0091` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.0135` n `770`
- 4h: commodity avg `0.1753` n `12`; crypto_alt avg `0.2765` n `230`; crypto_major avg `0.4368` n `8`; equity avg `0.0065` n `96`; fx avg `-0.021` n `6`; index avg `-0.0238` n `25`; metal avg `-0.0175` n `20`; unknown avg `0.0863` n `770`
- 24h: commodity avg `0.3512` n `12`; crypto_alt avg `-0.3501` n `230`; crypto_major avg `0.4076` n `8`; equity avg `-0.2425` n `96`; fx avg `-0.0969` n `6`; index avg `0.0371` n `25`; metal avg `0.0256` n `20`; unknown avg `-0.0069` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
