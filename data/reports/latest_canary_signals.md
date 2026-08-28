# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T13:22:27.452080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0943` n `12`; crypto_alt avg `-0.2974` n `231`; crypto_major avg `-0.0601` n `8`; equity avg `-0.1237` n `127`; fx avg `0.0016` n `6`; index avg `-0.0099` n `26`; metal avg `-0.0695` n `20`; unknown avg `0.0091` n `793`
- 1h: commodity avg `0.0984` n `12`; crypto_alt avg `-0.4253` n `231`; crypto_major avg `-0.1203` n `8`; equity avg `-0.0706` n `127`; fx avg `-0.0089` n `6`; index avg `0.011` n `26`; metal avg `0.0282` n `20`; unknown avg `-0.2567` n `792`
- 4h: commodity avg `-0.1161` n `12`; crypto_alt avg `-0.2278` n `231`; crypto_major avg `-0.1044` n `8`; equity avg `-0.0194` n `127`; fx avg `0.0222` n `6`; index avg `0.0292` n `26`; metal avg `0.1508` n `20`; unknown avg `-0.0662` n `792`
- 24h: commodity avg `-0.0795` n `12`; crypto_alt avg `-0.9977` n `231`; crypto_major avg `-0.1503` n `8`; equity avg `-0.8172` n `127`; fx avg `-0.1111` n `6`; index avg `0.021` n `26`; metal avg `0.8486` n `20`; unknown avg `0.4438` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
