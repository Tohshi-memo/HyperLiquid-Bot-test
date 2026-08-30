# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T02:52:23.087713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.1925` n `231`; crypto_major avg `0.1253` n `8`; equity avg `-0.0039` n `128`; fx avg `-0.0006` n `6`; index avg `0.0061` n `26`; metal avg `0.0029` n `20`; unknown avg `-0.144` n `793`
- 1h: commodity avg `0.0004` n `12`; crypto_alt avg `0.3166` n `231`; crypto_major avg `0.1526` n `8`; equity avg `0.02` n `128`; fx avg `0.0013` n `6`; index avg `0.0087` n `26`; metal avg `0.0037` n `20`; unknown avg `-0.1643` n `793`
- 4h: commodity avg `-0.0118` n `12`; crypto_alt avg `0.0419` n `231`; crypto_major avg `0.0581` n `8`; equity avg `0.0299` n `128`; fx avg `0.0196` n `6`; index avg `-0.0016` n `26`; metal avg `0.0061` n `20`; unknown avg `3.4414` n `793`
- 24h: commodity avg `-0.0134` n `12`; crypto_alt avg `0.3589` n `231`; crypto_major avg `0.9224` n `8`; equity avg `0.3426` n `128`; fx avg `-0.0064` n `6`; index avg `0.0731` n `26`; metal avg `0.111` n `20`; unknown avg `0.0893` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2114`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
