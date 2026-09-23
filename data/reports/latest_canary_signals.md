# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T01:52:28.826637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `-0.4598` n `234`; crypto_major avg `-0.2293` n `8`; equity avg `-0.1163` n `140`; fx avg `0.006` n `6`; index avg `-0.0131` n `26`; metal avg `-0.0461` n `20`; unknown avg `0.5977` n `945`
- 1h: commodity avg `0.0092` n `12`; crypto_alt avg `-0.48` n `234`; crypto_major avg `-0.347` n `8`; equity avg `-0.2623` n `140`; fx avg `-0.0317` n `6`; index avg `-0.0366` n `26`; metal avg `-0.1875` n `20`; unknown avg `0.5567` n `943`
- 4h: commodity avg `0.0597` n `12`; crypto_alt avg `0.4201` n `234`; crypto_major avg `0.1065` n `8`; equity avg `-0.1867` n `140`; fx avg `-0.0789` n `6`; index avg `-0.0822` n `26`; metal avg `-0.1574` n `20`; unknown avg `0.5661` n `936`
- 24h: commodity avg `0.0685` n `12`; crypto_alt avg `2.4802` n `234`; crypto_major avg `1.229` n `8`; equity avg `0.4278` n `140`; fx avg `-0.2239` n `6`; index avg `-0.0015` n `26`; metal avg `0.1073` n `20`; unknown avg `0.9837` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
