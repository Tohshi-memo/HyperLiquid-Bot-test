# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T18:07:29.969823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `-0.0437` n `233`; crypto_major avg `-0.0874` n `8`; equity avg `0.0026` n `136`; fx avg `-0.0063` n `6`; index avg `-0.0046` n `26`; metal avg `0.0017` n `20`; unknown avg `0.0664` n `836`
- 1h: commodity avg `0.0392` n `12`; crypto_alt avg `-0.1344` n `233`; crypto_major avg `-0.1853` n `8`; equity avg `-0.0269` n `136`; fx avg `-0.0091` n `6`; index avg `-0.005` n `26`; metal avg `-0.009` n `20`; unknown avg `4.4765` n `836`
- 4h: commodity avg `0.0397` n `12`; crypto_alt avg `0.169` n `233`; crypto_major avg `-0.2498` n `8`; equity avg `0.0094` n `136`; fx avg `-0.0102` n `6`; index avg `0.0032` n `26`; metal avg `0.0056` n `20`; unknown avg `2.8182` n `790`
- 24h: commodity avg `-0.0687` n `12`; crypto_alt avg `1.2375` n `233`; crypto_major avg `0.1998` n `8`; equity avg `-0.2685` n `136`; fx avg `-0.0245` n `6`; index avg `-0.0194` n `26`; metal avg `-0.0253` n `20`; unknown avg `1.1606` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
