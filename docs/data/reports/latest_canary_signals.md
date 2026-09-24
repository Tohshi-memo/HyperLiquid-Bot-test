# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T09:07:31.188743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1548` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1253` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0854` n `12`; crypto_alt avg `-0.0462` n `234`; crypto_major avg `0.0097` n `8`; equity avg `0.1116` n `141`; fx avg `0.0107` n `6`; index avg `0.0153` n `26`; metal avg `-0.003` n `20`; unknown avg `0.261` n `943`
- 1h: commodity avg `0.0851` n `12`; crypto_alt avg `-1.3502` n `234`; crypto_major avg `-1.1982` n `8`; equity avg `-0.6469` n `141`; fx avg `0.0599` n `6`; index avg `-0.0729` n `26`; metal avg `-0.1927` n `20`; unknown avg `1.0093` n `943`
- 4h: commodity avg `0.4503` n `12`; crypto_alt avg `-1.5342` n `234`; crypto_major avg `-1.3179` n `8`; equity avg `-1.1385` n `141`; fx avg `0.0772` n `6`; index avg `-0.1631` n `26`; metal avg `-0.173` n `20`; unknown avg `3.2604` n `921`
- 24h: commodity avg `0.765` n `12`; crypto_alt avg `-4.5851` n `234`; crypto_major avg `-3.7698` n `8`; equity avg `-2.6994` n `140`; fx avg `0.0188` n `6`; index avg `-0.4901` n `26`; metal avg `-0.5024` n `20`; unknown avg `587.1691` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
