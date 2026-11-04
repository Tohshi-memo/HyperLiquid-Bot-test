# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T19:07:33.896952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0579` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0473` n `13`; crypto_alt avg `0.0594` n `239`; crypto_major avg `-0.0276` n `8`; equity avg `0.2356` n `158`; fx avg `-0.0037` n `6`; index avg `0.0325` n `27`; metal avg `0.0128` n `20`; unknown avg `0.2096` n `1258`
- 1h: commodity avg `-0.087` n `13`; crypto_alt avg `-0.4287` n `239`; crypto_major avg `-0.4547` n `8`; equity avg `-0.267` n `158`; fx avg `-0.0161` n `6`; index avg `-0.0312` n `27`; metal avg `-0.0568` n `20`; unknown avg `0.901` n `1258`
- 4h: commodity avg `-1.1681` n `13`; crypto_alt avg `-1.4345` n `239`; crypto_major avg `-1.1138` n `8`; equity avg `-1.5554` n `158`; fx avg `-0.0473` n `6`; index avg `-0.0559` n `27`; metal avg `0.2066` n `20`; unknown avg `3.9522` n `1252`
- 24h: commodity avg `-1.7073` n `13`; crypto_alt avg `1.7792` n `239`; crypto_major avg `2.1734` n `8`; equity avg `-0.5665` n `158`; fx avg `0.0291` n `6`; index avg `0.1628` n `27`; metal avg `1.2282` n `20`; unknown avg `0.6186` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2715`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
