# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T03:22:28.517417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `13`; crypto_alt avg `-0.0657` n `237`; crypto_major avg `-0.0438` n `8`; equity avg `0.171` n `151`; fx avg `0.0028` n `6`; index avg `0.0412` n `26`; metal avg `0.0149` n `20`; unknown avg `-0.123` n `1194`
- 1h: commodity avg `0.0155` n `13`; crypto_alt avg `-0.0104` n `237`; crypto_major avg `0.1726` n `8`; equity avg `0.5751` n `151`; fx avg `0.0347` n `6`; index avg `0.0855` n `26`; metal avg `0.052` n `20`; unknown avg `-0.4816` n `1192`
- 4h: commodity avg `-0.0838` n `13`; crypto_alt avg `0.9283` n `237`; crypto_major avg `0.9128` n `8`; equity avg `1.8522` n `151`; fx avg `0.0004` n `6`; index avg `0.3446` n `26`; metal avg `0.1211` n `20`; unknown avg `3.875` n `1128`
- 24h: commodity avg `-0.4097` n `13`; crypto_alt avg `-0.1391` n `237`; crypto_major avg `0.6901` n `8`; equity avg `2.8835` n `151`; fx avg `-0.0165` n `6`; index avg `0.5349` n `26`; metal avg `0.3195` n `20`; unknown avg `3.3206` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.201`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1472`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1105`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0946`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0649`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0624`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
