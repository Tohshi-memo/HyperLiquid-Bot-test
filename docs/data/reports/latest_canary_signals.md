# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T18:07:17.174747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `-0.0355` n `228`; crypto_major avg `-0.1661` n `8`; equity avg `-0.0096` n `67`; fx avg `-0.0098` n `6`; index avg `0.0016` n `23`; metal avg `0.0333` n `18`; unknown avg `0.0538` n `396`
- 1h: commodity avg `0.11` n `12`; crypto_alt avg `-0.0034` n `228`; crypto_major avg `-0.1613` n `8`; equity avg `0.0303` n `67`; fx avg `-0.0037` n `6`; index avg `0.0793` n `23`; metal avg `-0.0223` n `18`; unknown avg `-0.0545` n `396`
- 4h: commodity avg `0.6446` n `12`; crypto_alt avg `0.1387` n `228`; crypto_major avg `-0.3535` n `8`; equity avg `-0.1728` n `67`; fx avg `-0.0032` n `6`; index avg `-0.1982` n `23`; metal avg `-0.2626` n `18`; unknown avg `-0.2276` n `396`
- 24h: commodity avg `-1.1278` n `12`; crypto_alt avg `0.4004` n `228`; crypto_major avg `1.9423` n `8`; equity avg `1.6251` n `67`; fx avg `0.077` n `6`; index avg `0.6602` n `23`; metal avg `0.5532` n `18`; unknown avg `0.7301` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
