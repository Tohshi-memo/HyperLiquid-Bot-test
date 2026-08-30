# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T03:07:48.251912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `12`; crypto_alt avg `-0.1022` n `231`; crypto_major avg `-0.1444` n `8`; equity avg `-0.0019` n `128`; fx avg `0.0033` n `6`; index avg `0.0074` n `26`; metal avg `-0.0095` n `20`; unknown avg `0.4674` n `793`
- 1h: commodity avg `0.0113` n `12`; crypto_alt avg `0.2433` n `231`; crypto_major avg `0.0342` n `8`; equity avg `0.0061` n `128`; fx avg `0.0047` n `6`; index avg `0.0069` n `26`; metal avg `-0.0055` n `20`; unknown avg `0.071` n `793`
- 4h: commodity avg `-0.003` n `12`; crypto_alt avg `-0.0899` n `231`; crypto_major avg `-0.1486` n `8`; equity avg `0.0272` n `128`; fx avg `0.0198` n `6`; index avg `0.0305` n `26`; metal avg `-0.0086` n `20`; unknown avg `3.6409` n `793`
- 24h: commodity avg `-0.0042` n `12`; crypto_alt avg `0.2852` n `231`; crypto_major avg `0.8025` n `8`; equity avg `0.3449` n `128`; fx avg `-0.0048` n `6`; index avg `0.0767` n `26`; metal avg `0.1018` n `20`; unknown avg `0.0915` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2063`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
