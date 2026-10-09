# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T21:52:29.205982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `13`; crypto_alt avg `0.0889` n `235`; crypto_major avg `-0.0292` n `8`; equity avg `0.0014` n `150`; fx avg `0.0006` n `6`; index avg `0.0025` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.0165` n `1116`
- 1h: commodity avg `-0.0719` n `13`; crypto_alt avg `0.3821` n `235`; crypto_major avg `0.1609` n `8`; equity avg `-0.0118` n `150`; fx avg `-0.0022` n `6`; index avg `0.0014` n `26`; metal avg `-0.019` n `20`; unknown avg `-0.0085` n `1098`
- 4h: commodity avg `-0.2603` n `13`; crypto_alt avg `0.2085` n `235`; crypto_major avg `-0.1296` n `8`; equity avg `-0.0146` n `150`; fx avg `0.0116` n `6`; index avg `0.0271` n `26`; metal avg `-0.0025` n `20`; unknown avg `2.5596` n `1026`
- 24h: commodity avg `-0.1762` n `13`; crypto_alt avg `1.823` n `235`; crypto_major avg `0.3268` n `8`; equity avg `0.8517` n `150`; fx avg `0.0104` n `6`; index avg `0.1557` n `26`; metal avg `0.601` n `20`; unknown avg `12.7572` n `901`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
