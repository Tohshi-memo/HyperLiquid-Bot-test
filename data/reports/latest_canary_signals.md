# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T13:07:28.810623+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0447` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0504` n `12`; crypto_alt avg `-0.2552` n `234`; crypto_major avg `-0.155` n `8`; equity avg `-0.0187` n `140`; fx avg `-0.0004` n `6`; index avg `-0.0017` n `26`; metal avg `0.0374` n `20`; unknown avg `5.2799` n `944`
- 1h: commodity avg `-0.0197` n `12`; crypto_alt avg `-0.3175` n `234`; crypto_major avg `-0.3667` n `8`; equity avg `0.0866` n `140`; fx avg `0.0008` n `6`; index avg `0.0048` n `26`; metal avg `-0.0973` n `20`; unknown avg `2.0956` n `944`
- 4h: commodity avg `0.1676` n `12`; crypto_alt avg `-1.1066` n `234`; crypto_major avg `-1.1169` n `8`; equity avg `-0.4402` n `140`; fx avg `-0.0239` n `6`; index avg `-0.0722` n `26`; metal avg `-0.1922` n `20`; unknown avg `3.9399` n `937`
- 24h: commodity avg `0.7411` n `12`; crypto_alt avg `1.2442` n `234`; crypto_major avg `-0.9412` n `8`; equity avg `0.4917` n `140`; fx avg `-0.0178` n `6`; index avg `-0.001` n `26`; metal avg `-0.4452` n `20`; unknown avg `3.8741` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
