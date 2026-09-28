# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T10:52:28.705145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0364` n `12`; crypto_alt avg `0.1089` n `234`; crypto_major avg `0.0646` n `8`; equity avg `0.1422` n `141`; fx avg `-0.0085` n `6`; index avg `0.0292` n `26`; metal avg `0.0218` n `20`; unknown avg `3.6201` n `962`
- 1h: commodity avg `0.0296` n `12`; crypto_alt avg `0.8179` n `234`; crypto_major avg `0.6035` n `8`; equity avg `0.0803` n `141`; fx avg `0.0163` n `6`; index avg `-0.0033` n `26`; metal avg `0.0529` n `20`; unknown avg `28.5425` n `960`
- 4h: commodity avg `0.4011` n `12`; crypto_alt avg `-0.4547` n `234`; crypto_major avg `0.3067` n `8`; equity avg `-0.4014` n `140`; fx avg `-0.0462` n `6`; index avg `-0.0273` n `23`; metal avg `-0.0831` n `18`; unknown avg `21.8776` n `924`
- 24h: commodity avg `-0.0461` n `12`; crypto_alt avg `-3.8051` n `234`; crypto_major avg `-2.6505` n `8`; equity avg `-2.7125` n `141`; fx avg `0.0285` n `6`; index avg `-0.2681` n `26`; metal avg `-0.8605` n `20`; unknown avg `6.1499` n `814`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
