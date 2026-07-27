# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T06:52:26.975341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.1692` n `230`; crypto_major avg `-0.1416` n `8`; equity avg `0.0236` n `100`; fx avg `-0.0025` n `6`; index avg `-0.0117` n `25`; metal avg `-0.0133` n `20`; unknown avg `-0.0516` n `775`
- 1h: commodity avg `-0.2629` n `12`; crypto_alt avg `-0.0147` n `230`; crypto_major avg `0.223` n `8`; equity avg `0.2418` n `100`; fx avg `0.0376` n `6`; index avg `0.0165` n `25`; metal avg `0.0897` n `20`; unknown avg `-0.0257` n `759`
- 4h: commodity avg `-0.464` n `12`; crypto_alt avg `0.0192` n `230`; crypto_major avg `0.6149` n `8`; equity avg `0.713` n `100`; fx avg `0.0393` n `6`; index avg `0.1372` n `25`; metal avg `0.0829` n `20`; unknown avg `0.0053` n `759`
- 24h: commodity avg `-0.9469` n `12`; crypto_alt avg `0.9659` n `230`; crypto_major avg `1.53` n `8`; equity avg `1.2908` n `100`; fx avg `0.1143` n `6`; index avg `0.1734` n `25`; metal avg `0.4256` n `20`; unknown avg `-0.0569` n `759`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
