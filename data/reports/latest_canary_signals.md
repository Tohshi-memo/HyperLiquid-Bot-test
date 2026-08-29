# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T16:07:25.163649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.04` n `12`; crypto_alt avg `-0.011` n `231`; crypto_major avg `0.078` n `8`; equity avg `-0.0041` n `128`; fx avg `0.0` n `6`; index avg `0.0046` n `26`; metal avg `-0.0026` n `20`; unknown avg `-0.0937` n `790`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `0.0009` n `231`; crypto_major avg `0.0415` n `8`; equity avg `-0.0091` n `128`; fx avg `-0.0015` n `6`; index avg `0.0011` n `26`; metal avg `0.0113` n `20`; unknown avg `-0.0962` n `786`
- 4h: commodity avg `-0.0126` n `12`; crypto_alt avg `0.9857` n `231`; crypto_major avg `0.8796` n `8`; equity avg `-0.011` n `128`; fx avg `-0.0015` n `6`; index avg `0.0047` n `26`; metal avg `0.0539` n `20`; unknown avg `0.2832` n `774`
- 24h: commodity avg `0.0826` n `12`; crypto_alt avg `0.0972` n `231`; crypto_major avg `-0.2475` n `8`; equity avg `-0.1977` n `128`; fx avg `-0.0591` n `6`; index avg `-0.0618` n `26`; metal avg `-0.2762` n `20`; unknown avg `-0.066` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2098`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
