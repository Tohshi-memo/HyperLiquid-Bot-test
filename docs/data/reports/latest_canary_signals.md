# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T11:52:27.257070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0294` n `12`; crypto_alt avg `0.1269` n `233`; crypto_major avg `0.0601` n `8`; equity avg `0.0021` n `136`; fx avg `0.0013` n `6`; index avg `-0.0016` n `26`; metal avg `0.0312` n `20`; unknown avg `0.052` n `838`
- 1h: commodity avg `0.0217` n `12`; crypto_alt avg `0.1023` n `233`; crypto_major avg `0.1406` n `8`; equity avg `0.0601` n `136`; fx avg `-0.0046` n `6`; index avg `-0.0025` n `26`; metal avg `0.0328` n `20`; unknown avg `0.0606` n `836`
- 4h: commodity avg `0.0603` n `12`; crypto_alt avg `0.1477` n `233`; crypto_major avg `0.4869` n `8`; equity avg `0.0605` n `136`; fx avg `-0.0069` n `6`; index avg `-0.0047` n `26`; metal avg `0.0401` n `20`; unknown avg `0.5176` n `830`
- 24h: commodity avg `0.0109` n `12`; crypto_alt avg `2.6566` n `233`; crypto_major avg `1.9979` n `8`; equity avg `0.214` n `136`; fx avg `-0.0385` n `6`; index avg `0.0975` n `26`; metal avg `0.0714` n `20`; unknown avg `1.1555` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
