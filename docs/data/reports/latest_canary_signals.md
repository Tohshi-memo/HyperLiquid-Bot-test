# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T22:07:24.313706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `0.1021` n `230`; crypto_major avg `0.1761` n `8`; equity avg `-0.0437` n `113`; fx avg `0.0072` n `6`; index avg `-0.0107` n `25`; metal avg `0.0429` n `20`; unknown avg `0.0951` n `786`
- 1h: commodity avg `0.0649` n `12`; crypto_alt avg `0.1718` n `230`; crypto_major avg `0.3025` n `8`; equity avg `-0.1127` n `113`; fx avg `0.006` n `6`; index avg `-0.0232` n `25`; metal avg `0.0281` n `20`; unknown avg `0.0252` n `785`
- 4h: commodity avg `-0.0086` n `12`; crypto_alt avg `0.5502` n `230`; crypto_major avg `0.933` n `8`; equity avg `0.5459` n `113`; fx avg `0.0045` n `6`; index avg `0.0233` n `25`; metal avg `0.0937` n `20`; unknown avg `0.5902` n `785`
- 24h: commodity avg `0.1228` n `12`; crypto_alt avg `-0.8638` n `230`; crypto_major avg `0.9214` n `8`; equity avg `1.1205` n `113`; fx avg `-0.0672` n `6`; index avg `0.0867` n `25`; metal avg `-0.184` n `20`; unknown avg `-0.0983` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2207`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.207`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1977`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
