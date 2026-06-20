# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T23:37:28.838253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `-0.0398` n `228`; crypto_major avg `-0.0421` n `8`; equity avg `-0.0393` n `78`; fx avg `0.001` n `6`; index avg `-0.0178` n `23`; metal avg `0.0038` n `18`; unknown avg `0.1041` n `701`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.0887` n `228`; crypto_major avg `-0.0863` n `8`; equity avg `0.0156` n `78`; fx avg `-0.0028` n `6`; index avg `-0.015` n `23`; metal avg `-0.0198` n `18`; unknown avg `1.8777` n `701`
- 4h: commodity avg `0.0509` n `12`; crypto_alt avg `0.7106` n `228`; crypto_major avg `0.8805` n `8`; equity avg `0.2227` n `78`; fx avg `0.0024` n `6`; index avg `0.0153` n `23`; metal avg `0.0296` n `18`; unknown avg `-0.4006` n `701`
- 24h: commodity avg `0.3128` n `12`; crypto_alt avg `1.1907` n `228`; crypto_major avg `1.6952` n `8`; equity avg `0.4082` n `78`; fx avg `0.0792` n `6`; index avg `0.0396` n `23`; metal avg `-0.0535` n `18`; unknown avg `-0.4179` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
