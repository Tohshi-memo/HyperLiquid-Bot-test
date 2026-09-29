# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T22:52:30.563677+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0308` n `12`; crypto_alt avg `0.0321` n `234`; crypto_major avg `0.05` n `8`; equity avg `-0.0027` n `142`; fx avg `-0.0109` n `6`; index avg `-0.0038` n `26`; metal avg `0.0128` n `20`; unknown avg `2.8657` n `962`
- 1h: commodity avg `0.05` n `12`; crypto_alt avg `-0.2554` n `234`; crypto_major avg `0.1366` n `8`; equity avg `0.0612` n `142`; fx avg `0.0023` n `6`; index avg `0.033` n `26`; metal avg `0.0109` n `20`; unknown avg `4.1088` n `942`
- 4h: commodity avg `0.011` n `12`; crypto_alt avg `-0.3996` n `234`; crypto_major avg `-0.1082` n `8`; equity avg `0.0725` n `142`; fx avg `0.0038` n `6`; index avg `0.0405` n `26`; metal avg `0.0827` n `20`; unknown avg `4.3418` n `872`
- 24h: commodity avg `-0.8994` n `12`; crypto_alt avg `0.8512` n `234`; crypto_major avg `0.007` n `8`; equity avg `0.7696` n `142`; fx avg `-0.1712` n `6`; index avg `0.0969` n `26`; metal avg `0.2668` n `20`; unknown avg `3099.0948` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1906`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1875`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
