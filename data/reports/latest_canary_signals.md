# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T09:52:27.933346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0438` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `-0.0914` n `234`; crypto_major avg `-0.1412` n `8`; equity avg `-0.0785` n `140`; fx avg `-0.0039` n `6`; index avg `-0.0159` n `26`; metal avg `-0.03` n `20`; unknown avg `-0.0593` n `945`
- 1h: commodity avg `0.0597` n `12`; crypto_alt avg `0.5449` n `234`; crypto_major avg `0.0829` n `8`; equity avg `0.0611` n `140`; fx avg `-0.0294` n `6`; index avg `-0.0045` n `26`; metal avg `-0.0599` n `20`; unknown avg `0.3927` n `943`
- 4h: commodity avg `0.2114` n `12`; crypto_alt avg `0.0221` n `234`; crypto_major avg `-1.0803` n `8`; equity avg `-0.1254` n `140`; fx avg `0.0657` n `6`; index avg `-0.0365` n `26`; metal avg `-0.2471` n `20`; unknown avg `0.015` n `921`
- 24h: commodity avg `0.645` n `12`; crypto_alt avg `3.3002` n `234`; crypto_major avg `0.353` n `8`; equity avg `0.8329` n `140`; fx avg `0.0145` n `6`; index avg `0.0514` n `26`; metal avg `-0.1297` n `20`; unknown avg `1.1376` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
