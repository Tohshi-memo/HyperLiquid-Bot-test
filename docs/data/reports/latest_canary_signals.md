# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T10:52:25.858921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `0.13` n `231`; crypto_major avg `0.112` n `8`; equity avg `0.0035` n `128`; fx avg `0.0006` n `6`; index avg `-0.0124` n `26`; metal avg `0.0043` n `20`; unknown avg `-0.0215` n `791`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `0.5672` n `231`; crypto_major avg `0.322` n `8`; equity avg `0.0259` n `128`; fx avg `-0.0007` n `6`; index avg `-0.0183` n `26`; metal avg `0.0023` n `20`; unknown avg `-0.1218` n `791`
- 4h: commodity avg `-0.0166` n `12`; crypto_alt avg `0.3055` n `231`; crypto_major avg `-0.0843` n `8`; equity avg `-0.0207` n `128`; fx avg `-0.0029` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0043` n `20`; unknown avg `-0.2514` n `791`
- 24h: commodity avg `-0.0118` n `12`; crypto_alt avg `1.5141` n `231`; crypto_major avg `0.8884` n `8`; equity avg `0.2586` n `128`; fx avg `0.0094` n `6`; index avg `0.0566` n `26`; metal avg `0.0881` n `20`; unknown avg `0.7329` n `716`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
