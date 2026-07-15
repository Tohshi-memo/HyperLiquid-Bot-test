# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T08:37:31.503541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.111` n `12`; crypto_alt avg `0.0764` n `230`; crypto_major avg `0.0808` n `8`; equity avg `0.1059` n `93`; fx avg `-0.0021` n `6`; index avg `0.01` n `25`; metal avg `0.0522` n `20`; unknown avg `0.0352` n `767`
- 1h: commodity avg `-0.1026` n `12`; crypto_alt avg `0.1666` n `230`; crypto_major avg `0.0939` n `8`; equity avg `-0.2114` n `93`; fx avg `0.0133` n `6`; index avg `-0.0274` n `25`; metal avg `0.1141` n `20`; unknown avg `0.0367` n `765`
- 4h: commodity avg `-0.0355` n `12`; crypto_alt avg `-0.1482` n `230`; crypto_major avg `-0.1338` n `8`; equity avg `-0.4747` n `93`; fx avg `-0.0076` n `6`; index avg `-0.1137` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.0711` n `747`
- 24h: commodity avg `-0.1145` n `12`; crypto_alt avg `1.4006` n `230`; crypto_major avg `2.893` n `8`; equity avg `0.985` n `92`; fx avg `0.0631` n `6`; index avg `0.3766` n `25`; metal avg `0.3101` n `20`; unknown avg `0.2377` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
