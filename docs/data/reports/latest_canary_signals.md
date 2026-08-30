# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T04:22:26.180337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.0072` n `231`; crypto_major avg `-0.0267` n `8`; equity avg `0.0083` n `128`; fx avg `0.0018` n `6`; index avg `-0.0095` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.1237` n `793`
- 1h: commodity avg `-0.0043` n `12`; crypto_alt avg `-0.0906` n `231`; crypto_major avg `-0.0018` n `8`; equity avg `0.0335` n `128`; fx avg `0.0018` n `6`; index avg `0.0047` n `26`; metal avg `0.0025` n `20`; unknown avg `-0.2811` n `793`
- 4h: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.1344` n `231`; crypto_major avg `-0.2148` n `8`; equity avg `0.0424` n `128`; fx avg `0.0048` n `6`; index avg `-0.0184` n `26`; metal avg `-0.0138` n `20`; unknown avg `-0.4002` n `793`
- 24h: commodity avg `-0.0108` n `12`; crypto_alt avg `0.4035` n `231`; crypto_major avg `0.73` n `8`; equity avg `0.3165` n `128`; fx avg `-0.0013` n `6`; index avg `0.0602` n `26`; metal avg `0.0924` n `20`; unknown avg `0.2375` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
