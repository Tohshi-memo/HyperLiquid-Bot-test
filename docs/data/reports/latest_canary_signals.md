# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T11:37:34.997843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3514` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0983` n `12`; crypto_alt avg `-0.3143` n `234`; crypto_major avg `-0.2253` n `8`; equity avg `-0.2094` n `140`; fx avg `-0.0185` n `6`; index avg `-0.0345` n `26`; metal avg `-0.0866` n `20`; unknown avg `-0.399` n `946`
- 1h: commodity avg `0.1831` n `12`; crypto_alt avg `-1.0626` n `234`; crypto_major avg `-0.602` n `8`; equity avg `-0.5653` n `140`; fx avg `0.0103` n `6`; index avg `-0.0722` n `26`; metal avg `-0.1756` n `20`; unknown avg `3.0991` n `944`
- 4h: commodity avg `0.279` n `12`; crypto_alt avg `-1.2454` n `234`; crypto_major avg `-1.4567` n `8`; equity avg `-0.6356` n `140`; fx avg `-0.0369` n `6`; index avg `-0.1053` n `26`; metal avg `-0.2326` n `20`; unknown avg `3.9553` n `937`
- 24h: commodity avg `0.7665` n `12`; crypto_alt avg `2.6097` n `234`; crypto_major avg `-0.0345` n `8`; equity avg `0.3454` n `140`; fx avg `0.018` n `6`; index avg `-0.0012` n `26`; metal avg `-0.1971` n `20`; unknown avg `7.4057` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
