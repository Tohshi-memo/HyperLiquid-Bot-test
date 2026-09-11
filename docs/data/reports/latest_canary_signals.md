# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T23:26:52.479445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0213` n `12`; crypto_alt avg `0.1449` n `233`; crypto_major avg `0.139` n `8`; equity avg `0.0295` n `136`; fx avg `0.0076` n `6`; index avg `-0.002` n `26`; metal avg `-0.0105` n `20`; unknown avg `0.0691` n `834`
- 1h: commodity avg `0.0093` n `12`; crypto_alt avg `-0.107` n `233`; crypto_major avg `-0.1965` n `8`; equity avg `0.003` n `136`; fx avg `0.0065` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0192` n `20`; unknown avg `2.9385` n `828`
- 4h: commodity avg `-0.1531` n `12`; crypto_alt avg `-0.2739` n `233`; crypto_major avg `-0.1913` n `8`; equity avg `-0.0107` n `136`; fx avg `-0.0241` n `6`; index avg `0.0013` n `26`; metal avg `-0.0267` n `20`; unknown avg `1.0099` n `788`
- 24h: commodity avg `-0.7538` n `12`; crypto_alt avg `0.7542` n `233`; crypto_major avg `1.3673` n `8`; equity avg `0.9263` n `136`; fx avg `-0.1878` n `6`; index avg `0.3299` n `26`; metal avg `0.255` n `20`; unknown avg `2.0394` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
