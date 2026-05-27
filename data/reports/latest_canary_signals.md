# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T02:37:21.668118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0818` n `12`; crypto_alt avg `0.0175` n `228`; crypto_major avg `0.0647` n `8`; equity avg `-0.0003` n `67`; fx avg `-0.0159` n `6`; index avg `0.0693` n `23`; metal avg `-0.0346` n `18`; unknown avg `0.0156` n `418`
- 1h: commodity avg `0.0675` n `12`; crypto_alt avg `-0.5936` n `228`; crypto_major avg `-0.1692` n `8`; equity avg `-0.1135` n `67`; fx avg `-0.0257` n `6`; index avg `0.0419` n `23`; metal avg `-0.3323` n `18`; unknown avg `-0.0883` n `418`
- 4h: commodity avg `-0.2731` n `12`; crypto_alt avg `-0.3228` n `228`; crypto_major avg `0.1974` n `8`; equity avg `0.1464` n `67`; fx avg `-0.0571` n `6`; index avg `0.2659` n `23`; metal avg `-0.2111` n `18`; unknown avg `0.5066` n `418`
- 24h: commodity avg `0.1221` n `12`; crypto_alt avg `-0.5179` n `228`; crypto_major avg `-0.3256` n `8`; equity avg `0.8157` n `67`; fx avg `-0.0846` n `6`; index avg `1.0763` n `23`; metal avg `-0.2711` n `18`; unknown avg `0.6598` n `397`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1706`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
