# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T06:37:24.431796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0154` n `12`; crypto_alt avg `0.0553` n `231`; crypto_major avg `0.0738` n `8`; equity avg `0.0143` n `128`; fx avg `0.0` n `6`; index avg `-0.0026` n `26`; metal avg `0.0082` n `20`; unknown avg `0.0121` n `791`
- 1h: commodity avg `0.0154` n `12`; crypto_alt avg `0.1745` n `231`; crypto_major avg `0.1675` n `8`; equity avg `0.0307` n `128`; fx avg `0.0104` n `6`; index avg `-0.0185` n `26`; metal avg `0.0117` n `20`; unknown avg `0.0352` n `759`
- 4h: commodity avg `0.018` n `12`; crypto_alt avg `0.4549` n `231`; crypto_major avg `0.1378` n `8`; equity avg `0.0403` n `128`; fx avg `0.0137` n `6`; index avg `0.0084` n `26`; metal avg `0.0096` n `20`; unknown avg `0.0105` n `759`
- 24h: commodity avg `0.0607` n `12`; crypto_alt avg `0.9673` n `231`; crypto_major avg `1.1442` n `8`; equity avg `0.3305` n `128`; fx avg `0.003` n `6`; index avg `0.0607` n `26`; metal avg `0.0985` n `20`; unknown avg `0.7783` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
