# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T21:26:57.489557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1128` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `-0.372` n `234`; crypto_major avg `-0.2682` n `8`; equity avg `-0.0219` n `140`; fx avg `0.0019` n `6`; index avg `-0.0204` n `26`; metal avg `0.0045` n `20`; unknown avg `0.7211` n `943`
- 1h: commodity avg `0.0346` n `12`; crypto_alt avg `-0.8596` n `234`; crypto_major avg `-0.5629` n `8`; equity avg `-0.0052` n `140`; fx avg `0.0027` n `6`; index avg `0.0077` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.3566` n `941`
- 4h: commodity avg `0.0697` n `12`; crypto_alt avg `-1.2333` n `234`; crypto_major avg `-1.0959` n `8`; equity avg `0.0843` n `140`; fx avg `-0.0396` n `6`; index avg `0.0169` n `26`; metal avg `0.0211` n `20`; unknown avg `152.6711` n `919`
- 24h: commodity avg `0.089` n `12`; crypto_alt avg `0.4802` n `234`; crypto_major avg `-0.2616` n `8`; equity avg `-0.0455` n `140`; fx avg `-0.0811` n `6`; index avg `0.0139` n `26`; metal avg `0.0018` n `20`; unknown avg `5.8355` n `820`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1623`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
