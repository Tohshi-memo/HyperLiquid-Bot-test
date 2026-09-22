# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T15:07:56.657075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.6233` n `234`; crypto_major avg `0.5064` n `8`; equity avg `-0.0563` n `140`; fx avg `-0.0178` n `6`; index avg `0.0023` n `26`; metal avg `0.0592` n `20`; unknown avg `1.1039` n `940`
- 1h: commodity avg `0.1609` n `12`; crypto_alt avg `-0.2501` n `234`; crypto_major avg `-0.2444` n `8`; equity avg `-0.4273` n `140`; fx avg `-0.0032` n `6`; index avg `-0.0516` n `26`; metal avg `0.0111` n `20`; unknown avg `4.1729` n `940`
- 4h: commodity avg `0.4904` n `12`; crypto_alt avg `1.0931` n `234`; crypto_major avg `0.8196` n `8`; equity avg `0.398` n `140`; fx avg `-0.015` n `6`; index avg `0.0683` n `26`; metal avg `0.1351` n `20`; unknown avg `3.9328` n `892`
- 24h: commodity avg `0.1152` n `12`; crypto_alt avg `0.2207` n `234`; crypto_major avg `0.6145` n `8`; equity avg `0.7605` n `140`; fx avg `-0.3005` n `6`; index avg `0.1701` n `26`; metal avg `-0.0029` n `20`; unknown avg `8665.2875` n `842`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
