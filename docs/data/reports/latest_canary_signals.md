# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T16:22:25.817587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `12`; crypto_alt avg `0.0175` n `233`; crypto_major avg `-0.0082` n `8`; equity avg `0.0222` n `136`; fx avg `0.0007` n `6`; index avg `0.0012` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.0752` n `838`
- 1h: commodity avg `0.0163` n `12`; crypto_alt avg `0.104` n `233`; crypto_major avg `-0.1236` n `8`; equity avg `0.0286` n `136`; fx avg `-0.0059` n `6`; index avg `0.0071` n `26`; metal avg `0.0064` n `20`; unknown avg `-0.4891` n `836`
- 4h: commodity avg `-0.0162` n `12`; crypto_alt avg `0.3011` n `233`; crypto_major avg `-0.047` n `8`; equity avg `0.0104` n `136`; fx avg `-0.0019` n `6`; index avg `0.0158` n `26`; metal avg `0.0126` n `20`; unknown avg `2.1726` n `824`
- 24h: commodity avg `-0.1812` n `12`; crypto_alt avg `0.7376` n `233`; crypto_major avg `-0.209` n `8`; equity avg `-0.1374` n `136`; fx avg `-0.0197` n `6`; index avg `0.0241` n `26`; metal avg `0.0112` n `20`; unknown avg `12.5191` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
