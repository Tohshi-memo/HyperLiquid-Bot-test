# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T01:22:28.003519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `12`; crypto_alt avg `0.1092` n `234`; crypto_major avg `0.106` n `8`; equity avg `-0.0668` n `140`; fx avg `0.0046` n `6`; index avg `-0.0117` n `26`; metal avg `0.0029` n `20`; unknown avg `0.1839` n `919`
- 1h: commodity avg `0.057` n `12`; crypto_alt avg `0.7303` n `234`; crypto_major avg `0.6694` n `8`; equity avg `-0.075` n `140`; fx avg `0.0139` n `6`; index avg `-0.0131` n `26`; metal avg `0.1089` n `20`; unknown avg `0.0666` n `911`
- 4h: commodity avg `-0.0165` n `12`; crypto_alt avg `1.1805` n `234`; crypto_major avg `0.8212` n `8`; equity avg `-0.2277` n `140`; fx avg `0.0835` n `6`; index avg `-0.101` n `26`; metal avg `0.1968` n `20`; unknown avg `-0.0858` n `837`
- 24h: commodity avg `-0.2369` n `12`; crypto_alt avg `3.8387` n `234`; crypto_major avg `2.377` n `8`; equity avg `1.3867` n `138`; fx avg `0.0556` n `6`; index avg `0.165` n `26`; metal avg `0.4407` n `20`; unknown avg `1.5432` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
