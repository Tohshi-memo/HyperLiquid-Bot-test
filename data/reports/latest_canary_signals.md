# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T15:37:32.136275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0562` n `12`; crypto_alt avg `-0.092` n `234`; crypto_major avg `-0.0396` n `8`; equity avg `0.0639` n `140`; fx avg `-0.0021` n `6`; index avg `0.0206` n `26`; metal avg `0.0126` n `20`; unknown avg `0.1539` n `942`
- 1h: commodity avg `0.0144` n `12`; crypto_alt avg `-0.3316` n `234`; crypto_major avg `-0.0699` n `8`; equity avg `0.2565` n `140`; fx avg `0.0094` n `6`; index avg `0.062` n `26`; metal avg `0.059` n `20`; unknown avg `0.5663` n `940`
- 4h: commodity avg `-0.2332` n `12`; crypto_alt avg `-0.3154` n `234`; crypto_major avg `0.529` n `8`; equity avg `0.9335` n `140`; fx avg `0.0035` n `6`; index avg `0.2064` n `26`; metal avg `-0.0411` n `20`; unknown avg `11.4855` n `856`
- 24h: commodity avg `-1.0247` n `12`; crypto_alt avg `6.1574` n `234`; crypto_major avg `6.0535` n `8`; equity avg `2.798` n `140`; fx avg `-0.0636` n `6`; index avg `0.5652` n `26`; metal avg `0.0584` n `20`; unknown avg `4.582` n `707`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
