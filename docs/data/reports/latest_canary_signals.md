# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T09:22:32.709349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3498` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1999` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0164` n `12`; crypto_alt avg `-0.6221` n `234`; crypto_major avg `-0.449` n `8`; equity avg `-0.043` n `141`; fx avg `-0.0162` n `6`; index avg `0.0008` n `26`; metal avg `-0.0139` n `20`; unknown avg `0.7235` n `945`
- 1h: commodity avg `-0.0803` n `12`; crypto_alt avg `-1.5282` n `234`; crypto_major avg `-1.2206` n `8`; equity avg `-0.3648` n `141`; fx avg `0.0014` n `6`; index avg `-0.0207` n `26`; metal avg `-0.0234` n `20`; unknown avg `0.2142` n `943`
- 4h: commodity avg `0.3808` n `12`; crypto_alt avg `-1.8845` n `234`; crypto_major avg `-1.4971` n `8`; equity avg `-1.074` n `141`; fx avg `0.0639` n `6`; index avg `-0.1473` n `26`; metal avg `-0.1553` n `20`; unknown avg `3.2454` n `921`
- 24h: commodity avg `0.7542` n `12`; crypto_alt avg `-5.4312` n `234`; crypto_major avg `-4.2607` n `8`; equity avg `-2.7806` n `140`; fx avg `0.0348` n `6`; index avg `-0.493` n `26`; metal avg `-0.522` n `20`; unknown avg `587.4714` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
