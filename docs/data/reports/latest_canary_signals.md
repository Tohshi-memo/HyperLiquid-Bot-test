# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T19:51:19.235176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.0873` n `230`; crypto_major avg `0.155` n `8`; equity avg `-0.0399` n `113`; fx avg `0.0007` n `6`; index avg `-0.0169` n `25`; metal avg `-0.0056` n `20`; unknown avg `0.093` n `785`
- 1h: commodity avg `0.0408` n `12`; crypto_alt avg `0.1864` n `230`; crypto_major avg `0.2718` n `8`; equity avg `0.1977` n `113`; fx avg `0.0068` n `6`; index avg `0.0245` n `25`; metal avg `-0.0065` n `20`; unknown avg `0.1653` n `785`
- 4h: commodity avg `0.0618` n `12`; crypto_alt avg `0.4889` n `230`; crypto_major avg `0.766` n `8`; equity avg `0.0778` n `113`; fx avg `0.0068` n `6`; index avg `-0.0406` n `25`; metal avg `-0.0429` n `20`; unknown avg `0.4323` n `785`
- 24h: commodity avg `0.1828` n `12`; crypto_alt avg `-1.8063` n `230`; crypto_major avg `-0.2143` n `8`; equity avg `0.4566` n `113`; fx avg `-0.0598` n `6`; index avg `0.0724` n `25`; metal avg `-0.2472` n `20`; unknown avg `-0.2933` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2043`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
