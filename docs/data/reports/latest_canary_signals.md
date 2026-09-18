# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T00:22:31.275296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0299` n `12`; crypto_alt avg `-0.2075` n `234`; crypto_major avg `-0.2211` n `8`; equity avg `0.0022` n `140`; fx avg `-0.0146` n `6`; index avg `0.0111` n `26`; metal avg `0.066` n `20`; unknown avg `0.8205` n `919`
- 1h: commodity avg `-0.0832` n `12`; crypto_alt avg `-0.0292` n `234`; crypto_major avg `-0.1655` n `8`; equity avg `-0.0801` n `140`; fx avg `0.028` n `6`; index avg `-0.0634` n `26`; metal avg `0.0632` n `20`; unknown avg `0.214` n `917`
- 4h: commodity avg `-0.0859` n `12`; crypto_alt avg `0.2865` n `234`; crypto_major avg `-0.041` n `8`; equity avg `-0.1093` n `140`; fx avg `0.0273` n `6`; index avg `-0.0749` n `26`; metal avg `0.1066` n `20`; unknown avg `0.3202` n `815`
- 24h: commodity avg `-0.1898` n `12`; crypto_alt avg `3.0007` n `234`; crypto_major avg `1.6142` n `8`; equity avg `1.5596` n `138`; fx avg `0.045` n `6`; index avg `0.215` n `26`; metal avg `0.5122` n `20`; unknown avg `1.8233` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
