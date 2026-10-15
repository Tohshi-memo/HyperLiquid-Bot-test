# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T22:22:28.321245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `13`; crypto_alt avg `-0.0925` n `236`; crypto_major avg `-0.0257` n `8`; equity avg `-0.0329` n `151`; fx avg `-0.008` n `6`; index avg `0.0001` n `26`; metal avg `-0.0114` n `20`; unknown avg `-0.0593` n `1128`
- 1h: commodity avg `0.0124` n `13`; crypto_alt avg `-0.018` n `236`; crypto_major avg `0.104` n `8`; equity avg `0.2739` n `151`; fx avg `0.0165` n `6`; index avg `0.024` n `26`; metal avg `-0.0102` n `20`; unknown avg `-0.0263` n `1110`
- 4h: commodity avg `-0.1903` n `13`; crypto_alt avg `0.4393` n `236`; crypto_major avg `0.5397` n `8`; equity avg `1.4794` n `151`; fx avg `-0.0169` n `6`; index avg `0.1551` n `26`; metal avg `0.093` n `20`; unknown avg `-0.0278` n `1028`
- 24h: commodity avg `-0.253` n `13`; crypto_alt avg `0.7469` n `236`; crypto_major avg `0.9297` n `8`; equity avg `1.1836` n `151`; fx avg `0.198` n `6`; index avg `0.034` n `26`; metal avg `0.4812` n `20`; unknown avg `24.3262` n `918`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.098`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0858`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0756`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0751`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0718`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0488`, n `666`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0479`, n `666`, weak_sample_signal
