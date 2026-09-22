# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T18:07:35.352113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1515` n `12`; crypto_alt avg `-0.1224` n `234`; crypto_major avg `-0.1548` n `8`; equity avg `-0.0068` n `140`; fx avg `0.0` n `6`; index avg `0.0112` n `26`; metal avg `0.1086` n `20`; unknown avg `0.0196` n `940`
- 1h: commodity avg `-0.2823` n `12`; crypto_alt avg `0.2383` n `234`; crypto_major avg `0.1205` n `8`; equity avg `0.1632` n `140`; fx avg `0.0005` n `6`; index avg `0.048` n `26`; metal avg `0.1704` n `20`; unknown avg `0.9184` n `940`
- 4h: commodity avg `-0.0555` n `12`; crypto_alt avg `0.727` n `234`; crypto_major avg `-0.0205` n `8`; equity avg `0.0368` n `140`; fx avg `-0.0051` n `6`; index avg `0.0212` n `26`; metal avg `0.2304` n `20`; unknown avg `1.8693` n `880`
- 24h: commodity avg `-0.1076` n `12`; crypto_alt avg `2.3793` n `234`; crypto_major avg `1.2081` n `8`; equity avg `0.8713` n `140`; fx avg `-0.2814` n `6`; index avg `0.1373` n `26`; metal avg `0.2347` n `20`; unknown avg `0.4623` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
