# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T09:07:28.604207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2834` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `0.5325` n `234`; crypto_major avg `0.3731` n `8`; equity avg `0.0832` n `140`; fx avg `0.0145` n `6`; index avg `0.0073` n `26`; metal avg `0.0033` n `20`; unknown avg `0.3196` n `943`
- 1h: commodity avg `0.0421` n `12`; crypto_alt avg `0.4413` n `234`; crypto_major avg `-0.2277` n `8`; equity avg `-0.0148` n `140`; fx avg `-0.0068` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0196` n `20`; unknown avg `0.7138` n `943`
- 4h: commodity avg `0.1963` n `12`; crypto_alt avg `-0.354` n `234`; crypto_major avg `-1.301` n `8`; equity avg `-0.1384` n `140`; fx avg `0.1518` n `6`; index avg `-0.0176` n `26`; metal avg `-0.2773` n `20`; unknown avg `0.503` n `921`
- 24h: commodity avg `0.3787` n `12`; crypto_alt avg `3.4816` n `234`; crypto_major avg `0.9945` n `8`; equity avg `1.1992` n `140`; fx avg `0.0311` n `6`; index avg `0.1285` n `26`; metal avg `0.0079` n `20`; unknown avg `1.6866` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
