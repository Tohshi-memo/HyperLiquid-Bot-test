# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T11:10:00.184902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2726` n `12`; crypto_alt avg `0.089` n `230`; crypto_major avg `0.1642` n `8`; equity avg `0.3213` n `113`; fx avg `-0.0309` n `6`; index avg `0.0555` n `25`; metal avg `0.0651` n `20`; unknown avg `-0.0109` n `785`
- 1h: commodity avg `-0.4844` n `12`; crypto_alt avg `0.0348` n `230`; crypto_major avg `0.16` n `8`; equity avg `0.6035` n `113`; fx avg `-0.0577` n `6`; index avg `0.1107` n `25`; metal avg `0.1038` n `20`; unknown avg `0.0544` n `785`
- 4h: commodity avg `-0.3865` n `12`; crypto_alt avg `0.079` n `230`; crypto_major avg `0.6027` n `8`; equity avg `0.6037` n `113`; fx avg `-0.0731` n `6`; index avg `0.1391` n `25`; metal avg `0.296` n `20`; unknown avg `0.0746` n `785`
- 24h: commodity avg `0.4519` n `12`; crypto_alt avg `-1.0073` n `230`; crypto_major avg `-0.269` n `8`; equity avg `-0.4483` n `113`; fx avg `-0.0392` n `6`; index avg `0.1339` n `25`; metal avg `0.5112` n `20`; unknown avg `0.1728` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1864`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
