# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T18:52:32.001554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0368` n `12`; crypto_alt avg `0.0265` n `234`; crypto_major avg `0.0304` n `8`; equity avg `-0.0269` n `140`; fx avg `-0.0081` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0052` n `20`; unknown avg `0.309` n `917`
- 1h: commodity avg `-0.0808` n `12`; crypto_alt avg `-0.1383` n `234`; crypto_major avg `-0.1952` n `8`; equity avg `-0.0043` n `140`; fx avg `0.0036` n `6`; index avg `-0.0173` n `26`; metal avg `-0.0867` n `20`; unknown avg `1.5738` n `915`
- 4h: commodity avg `0.123` n `12`; crypto_alt avg `0.7003` n `234`; crypto_major avg `-0.1369` n `8`; equity avg `0.0882` n `140`; fx avg `0.0089` n `6`; index avg `0.0334` n `26`; metal avg `-0.1273` n `20`; unknown avg `4.393` n `907`
- 24h: commodity avg `-0.03` n `12`; crypto_alt avg `4.4965` n `234`; crypto_major avg `1.9577` n `8`; equity avg `2.3844` n `138`; fx avg `0.0647` n `6`; index avg `0.4027` n `26`; metal avg `0.5249` n `20`; unknown avg `3.086` n `715`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
