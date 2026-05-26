# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T02:52:16.008114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `12`; crypto_alt avg `0.1062` n `228`; crypto_major avg `-0.028` n `8`; equity avg `-0.0187` n `67`; fx avg `-0.0166` n `6`; index avg `-0.0261` n `23`; metal avg `-0.1503` n `18`; unknown avg `0.2625` n `407`
- 1h: commodity avg `-0.2425` n `12`; crypto_alt avg `-0.0005` n `228`; crypto_major avg `-0.0676` n `8`; equity avg `0.1461` n `67`; fx avg `-0.0036` n `6`; index avg `0.044` n `23`; metal avg `0.1739` n `18`; unknown avg `0.2994` n `407`
- 4h: commodity avg `0.4678` n `12`; crypto_alt avg `-1.2464` n `228`; crypto_major avg `-1.0354` n `8`; equity avg `-0.8304` n `67`; fx avg `-0.1073` n `6`; index avg `-0.2746` n `23`; metal avg `-0.9826` n `18`; unknown avg `1.4433` n `405`
- 24h: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.0835` n `228`; crypto_major avg `-0.9636` n `8`; equity avg `-0.2849` n `67`; fx avg `0.0032` n `6`; index avg `0.0615` n `23`; metal avg `-0.3418` n `18`; unknown avg `1.4453` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
