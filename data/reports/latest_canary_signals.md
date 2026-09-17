# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T15:52:29.211133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.017` n `12`; crypto_alt avg `0.2384` n `234`; crypto_major avg `0.1918` n `8`; equity avg `0.1652` n `138`; fx avg `0.0049` n `6`; index avg `0.0124` n `26`; metal avg `0.0319` n `20`; unknown avg `0.4297` n `919`
- 1h: commodity avg `0.019` n `12`; crypto_alt avg `0.3476` n `234`; crypto_major avg `0.1893` n `8`; equity avg `0.05` n `138`; fx avg `-0.014` n `6`; index avg `0.0345` n `26`; metal avg `0.0149` n `20`; unknown avg `0.3509` n `915`
- 4h: commodity avg `0.1055` n `12`; crypto_alt avg `1.0` n `234`; crypto_major avg `1.3636` n `8`; equity avg `0.7609` n `138`; fx avg `-0.0658` n `6`; index avg `0.1694` n `26`; metal avg `0.26` n `20`; unknown avg `1.3715` n `891`
- 24h: commodity avg `-0.1524` n `12`; crypto_alt avg `4.9031` n `234`; crypto_major avg `2.7327` n `8`; equity avg `1.5377` n `138`; fx avg `0.0292` n `6`; index avg `0.2066` n `26`; metal avg `0.1672` n `20`; unknown avg `0.2289` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
