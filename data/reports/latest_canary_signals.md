# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T03:52:24.324329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.1341` n `231`; crypto_major avg `-0.0762` n `8`; equity avg `0.0123` n `128`; fx avg `0.0012` n `6`; index avg `-0.0064` n `26`; metal avg `0.002` n `20`; unknown avg `0.0465` n `793`
- 1h: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.0114` n `231`; crypto_major avg `-0.1356` n `8`; equity avg `0.009` n `128`; fx avg `0.0051` n `6`; index avg `-0.0123` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.1623` n `793`
- 4h: commodity avg `-0.0148` n `12`; crypto_alt avg `-0.0525` n `231`; crypto_major avg `-0.195` n `8`; equity avg `0.0226` n `128`; fx avg `0.0134` n `6`; index avg `0.0093` n `26`; metal avg `-0.0046` n `20`; unknown avg `3.4945` n `793`
- 24h: commodity avg `-0.0335` n `12`; crypto_alt avg `0.5592` n `231`; crypto_major avg `0.8016` n `8`; equity avg `0.345` n `128`; fx avg `-0.0012` n `6`; index avg `0.0607` n `26`; metal avg `0.0997` n `20`; unknown avg `0.1263` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1851`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
