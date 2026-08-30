# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T06:22:30.243440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `0.061` n `231`; crypto_major avg `0.0796` n `8`; equity avg `-0.0062` n `128`; fx avg `0.0016` n `6`; index avg `-0.0001` n `26`; metal avg `0.0006` n `20`; unknown avg `0.0462` n `793`
- 1h: commodity avg `0.0037` n `12`; crypto_alt avg `0.2473` n `231`; crypto_major avg `0.0862` n `8`; equity avg `0.0079` n `128`; fx avg `0.0099` n `6`; index avg `-0.0123` n `26`; metal avg `0.0048` n `20`; unknown avg `-0.0349` n `761`
- 4h: commodity avg `0.0027` n `12`; crypto_alt avg `0.4321` n `231`; crypto_major avg `0.0411` n `8`; equity avg `0.015` n `128`; fx avg `0.0163` n `6`; index avg `0.0139` n `26`; metal avg `0.0026` n `20`; unknown avg `-0.1085` n `761`
- 24h: commodity avg `0.0403` n `12`; crypto_alt avg `1.0601` n `231`; crypto_major avg `1.2624` n `8`; equity avg `0.3272` n `128`; fx avg `0.0025` n `6`; index avg `0.0622` n `26`; metal avg `0.0902` n `20`; unknown avg `0.1198` n `712`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
