# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T01:22:32.175759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0867` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.1516` n `234`; crypto_major avg `-0.2812` n `8`; equity avg `-0.1625` n `140`; fx avg `0.0081` n `6`; index avg `-0.0283` n `26`; metal avg `-0.1062` n `20`; unknown avg `-0.0736` n `944`
- 1h: commodity avg `0.0573` n `12`; crypto_alt avg `-0.5061` n `234`; crypto_major avg `-1.1291` n `8`; equity avg `-0.2409` n `140`; fx avg `-0.0444` n `6`; index avg `-0.0424` n `26`; metal avg `-0.1089` n `20`; unknown avg `0.5613` n `942`
- 4h: commodity avg `0.1534` n `12`; crypto_alt avg `0.2528` n `234`; crypto_major avg `-0.6442` n `8`; equity avg `0.3012` n `140`; fx avg `-0.1444` n `6`; index avg `0.0459` n `26`; metal avg `0.0356` n `20`; unknown avg `0.7395` n `936`
- 24h: commodity avg `-0.1464` n `12`; crypto_alt avg `2.5867` n `234`; crypto_major avg `3.2176` n `8`; equity avg `2.1519` n `140`; fx avg `-0.2117` n `6`; index avg `0.4965` n `26`; metal avg `-0.054` n `20`; unknown avg `13.2949` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
