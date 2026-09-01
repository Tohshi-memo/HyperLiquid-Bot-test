# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T19:52:30.112330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0661` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.0856` n `232`; crypto_major avg `-0.1201` n `8`; equity avg `-0.0993` n `131`; fx avg `0.0074` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0163` n `20`; unknown avg `0.4477` n `793`
- 1h: commodity avg `0.0701` n `12`; crypto_alt avg `0.4466` n `232`; crypto_major avg `0.318` n `8`; equity avg `0.2467` n `131`; fx avg `0.0018` n `6`; index avg `0.0453` n `26`; metal avg `-0.0471` n `20`; unknown avg `1.5502` n `791`
- 4h: commodity avg `0.5827` n `12`; crypto_alt avg `-0.9361` n `232`; crypto_major avg `-1.2948` n `8`; equity avg `-0.8263` n `131`; fx avg `0.0164` n `6`; index avg `-0.2287` n `26`; metal avg `-0.414` n `20`; unknown avg `0.6218` n `791`
- 24h: commodity avg `0.8824` n `12`; crypto_alt avg `-0.1128` n `232`; crypto_major avg `-2.0385` n `8`; equity avg `-1.9652` n `130`; fx avg `0.0386` n `6`; index avg `-0.3677` n `26`; metal avg `-0.9544` n `20`; unknown avg `0.0157` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0384`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0356`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0336`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0323`, n `668`, weak_sample_signal
