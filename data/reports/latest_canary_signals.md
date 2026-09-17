# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T18:37:28.862040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0206` n `12`; crypto_alt avg `-0.2069` n `234`; crypto_major avg `-0.2871` n `8`; equity avg `-0.0685` n `140`; fx avg `0.0029` n `6`; index avg `-0.016` n `26`; metal avg `-0.0618` n `20`; unknown avg `1.8122` n `917`
- 1h: commodity avg `-0.0335` n `12`; crypto_alt avg `-0.2296` n `234`; crypto_major avg `-0.4928` n `8`; equity avg `0.0314` n `140`; fx avg `0.0028` n `6`; index avg `-0.0056` n `26`; metal avg `-0.082` n `20`; unknown avg `1.2793` n `915`
- 4h: commodity avg `0.1664` n `12`; crypto_alt avg `0.2308` n `234`; crypto_major avg `-0.5926` n `8`; equity avg `0.1569` n `140`; fx avg `0.0116` n `6`; index avg `0.0072` n `26`; metal avg `-0.1793` n `20`; unknown avg `3.2814` n `907`
- 24h: commodity avg `-0.0299` n `12`; crypto_alt avg `5.329` n `234`; crypto_major avg `2.5961` n `8`; equity avg `2.4341` n `138`; fx avg `0.0634` n `6`; index avg `0.4187` n `26`; metal avg `0.5571` n `20`; unknown avg `2.47` n `715`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
