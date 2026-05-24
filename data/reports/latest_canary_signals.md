# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T05:07:15.194059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.2332` n `228`; crypto_major avg `0.0351` n `8`; equity avg `0.0228` n `67`; fx avg `0.0003` n `6`; index avg `0.0119` n `23`; metal avg `0.0054` n `18`; unknown avg `-0.0284` n `396`
- 1h: commodity avg `-0.0148` n `12`; crypto_alt avg `-0.1386` n `228`; crypto_major avg `0.0182` n `8`; equity avg `0.2391` n `67`; fx avg `0.0356` n `6`; index avg `0.0027` n `23`; metal avg `-0.0363` n `18`; unknown avg `-0.1404` n `396`
- 4h: commodity avg `-0.2644` n `12`; crypto_alt avg `-0.7322` n `228`; crypto_major avg `-0.0596` n `8`; equity avg `0.2198` n `67`; fx avg `0.0188` n `6`; index avg `0.1303` n `23`; metal avg `0.1982` n `18`; unknown avg `-0.7605` n `396`
- 24h: commodity avg `-3.0587` n `12`; crypto_alt avg `1.755` n `228`; crypto_major avg `2.505` n `8`; equity avg `2.3825` n `67`; fx avg `0.0692` n `6`; index avg `1.2246` n `23`; metal avg `1.2115` n `18`; unknown avg `1.8341` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
