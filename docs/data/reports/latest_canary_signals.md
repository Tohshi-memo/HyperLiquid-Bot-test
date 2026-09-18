# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T00:29:33.595317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.2693` n `234`; crypto_major avg `-0.2316` n `8`; equity avg `-0.0209` n `140`; fx avg `0.0143` n `6`; index avg `0.0054` n `26`; metal avg `0.0467` n `20`; unknown avg `-0.2391` n `919`
- 1h: commodity avg `-0.0732` n `12`; crypto_alt avg `-0.0907` n `234`; crypto_major avg `-0.1759` n `8`; equity avg `-0.1032` n `140`; fx avg `0.057` n `6`; index avg `-0.0691` n `26`; metal avg `0.0439` n `20`; unknown avg `0.1299` n `917`
- 4h: commodity avg `-0.0759` n `12`; crypto_alt avg `0.2243` n `234`; crypto_major avg `-0.0513` n `8`; equity avg `-0.1323` n `140`; fx avg `0.0562` n `6`; index avg `-0.0805` n `26`; metal avg `0.0873` n `20`; unknown avg `0.2526` n `815`
- 24h: commodity avg `-0.1798` n `12`; crypto_alt avg `2.9361` n `234`; crypto_major avg `1.6044` n `8`; equity avg `1.5343` n `138`; fx avg `0.074` n `6`; index avg `0.2092` n `26`; metal avg `0.4926` n `20`; unknown avg `1.8218` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
