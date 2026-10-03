# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T17:22:33.250833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `13`; crypto_alt avg `0.2053` n `235`; crypto_major avg `0.1449` n `8`; equity avg `0.0015` n `143`; fx avg `-0.0005` n `6`; index avg `0.0009` n `26`; metal avg `0.002` n `20`; unknown avg `-0.0239` n `1078`
- 1h: commodity avg `0.1627` n `13`; crypto_alt avg `0.436` n `235`; crypto_major avg `0.439` n `8`; equity avg `0.0238` n `143`; fx avg `-0.0057` n `6`; index avg `0.0049` n `26`; metal avg `-0.0049` n `20`; unknown avg `-0.1145` n `1076`
- 4h: commodity avg `0.2003` n `13`; crypto_alt avg `1.1965` n `235`; crypto_major avg `0.7255` n `8`; equity avg `0.0835` n `143`; fx avg `-0.0064` n `6`; index avg `0.0268` n `26`; metal avg `0.0027` n `20`; unknown avg `-0.1894` n `950`
- 24h: commodity avg `0.3502` n `13`; crypto_alt avg `-0.0354` n `235`; crypto_major avg `0.0048` n `8`; equity avg `0.2424` n `143`; fx avg `-0.0514` n `6`; index avg `0.0562` n `26`; metal avg `0.1056` n `20`; unknown avg `-0.1337` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1853`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
