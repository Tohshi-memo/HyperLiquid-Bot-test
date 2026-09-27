# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T21:52:28.497075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `12`; crypto_alt avg `0.3829` n `234`; crypto_major avg `0.3004` n `8`; equity avg `-0.0376` n `141`; fx avg `0.0094` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0093` n `20`; unknown avg `1.168` n `956`
- 1h: commodity avg `0.0339` n `12`; crypto_alt avg `0.3092` n `234`; crypto_major avg `0.0783` n `8`; equity avg `-0.0206` n `141`; fx avg `-0.0161` n `6`; index avg `0.0115` n `26`; metal avg `-0.0084` n `20`; unknown avg `3.2221` n `918`
- 4h: commodity avg `0.0776` n `12`; crypto_alt avg `0.3313` n `234`; crypto_major avg `0.1086` n `8`; equity avg `0.0094` n `141`; fx avg `-0.0324` n `6`; index avg `0.0135` n `26`; metal avg `-0.0048` n `20`; unknown avg `3.5587` n `886`
- 24h: commodity avg `-0.0802` n `12`; crypto_alt avg `1.1961` n `234`; crypto_major avg `0.436` n `8`; equity avg `0.3761` n `141`; fx avg `-0.0387` n `6`; index avg `0.0555` n `26`; metal avg `-0.0223` n `20`; unknown avg `9.5892` n `829`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
