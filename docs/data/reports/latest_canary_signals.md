# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T00:19:39.563858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.026` n `12`; crypto_alt avg `0.1643` n `228`; crypto_major avg `-0.0227` n `8`; equity avg `0.0157` n `78`; fx avg `0.121` n `6`; index avg `-0.0027` n `23`; metal avg `0.0015` n `18`; unknown avg `-0.0302` n `701`
- 1h: commodity avg `0.0127` n `12`; crypto_alt avg `0.0261` n `228`; crypto_major avg `-0.2196` n `8`; equity avg `-0.0561` n `78`; fx avg `-0.0005` n `6`; index avg `-0.026` n `23`; metal avg `-0.0117` n `18`; unknown avg `0.179` n `701`
- 4h: commodity avg `0.0566` n `12`; crypto_alt avg `0.8015` n `228`; crypto_major avg `0.5751` n `8`; equity avg `0.1242` n `78`; fx avg `0.0023` n `6`; index avg `0.0116` n `23`; metal avg `0.0125` n `18`; unknown avg `-0.2019` n `701`
- 24h: commodity avg `0.3443` n `12`; crypto_alt avg `1.0638` n `228`; crypto_major avg `1.4532` n `8`; equity avg `0.3775` n `78`; fx avg `0.0485` n `6`; index avg `0.0151` n `23`; metal avg `-0.0568` n `18`; unknown avg `-0.3785` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
