# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T19:07:25.563894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.026` n `233`; crypto_major avg `-0.0051` n `8`; equity avg `-0.0022` n `136`; fx avg `0.0088` n `6`; index avg `0.0016` n `26`; metal avg `-0.0005` n `20`; unknown avg `2.1428` n `836`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `-0.0921` n `233`; crypto_major avg `-0.1294` n `8`; equity avg `-0.0252` n `136`; fx avg `0.0138` n `6`; index avg `0.0006` n `26`; metal avg `0.0077` n `20`; unknown avg `-0.0371` n `796`
- 4h: commodity avg `0.0594` n `12`; crypto_alt avg `-0.2041` n `233`; crypto_major avg `-0.5048` n `8`; equity avg `-0.0281` n `136`; fx avg `0.0032` n `6`; index avg `-0.0026` n `26`; metal avg `0.0158` n `20`; unknown avg `0.2968` n `782`
- 24h: commodity avg `-0.2085` n `12`; crypto_alt avg `1.59` n `233`; crypto_major avg `0.2487` n `8`; equity avg `-0.0322` n `136`; fx avg `-0.0288` n `6`; index avg `0.0314` n `26`; metal avg `0.0452` n `20`; unknown avg `1.219` n `692`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
