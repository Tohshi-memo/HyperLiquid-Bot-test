# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T09:07:26.283136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0791` n `13`; crypto_alt avg `-0.2532` n `239`; crypto_major avg `-0.1931` n `8`; equity avg `-0.5042` n `162`; fx avg `-0.021` n `6`; index avg `-0.0483` n `27`; metal avg `-0.0561` n `20`; unknown avg `18.8315` n `1260`
- 1h: commodity avg `0.0623` n `13`; crypto_alt avg `-0.41` n `239`; crypto_major avg `-0.5147` n `8`; equity avg `-0.6919` n `162`; fx avg `-0.0298` n `6`; index avg `-0.0697` n `27`; metal avg `0.0118` n `20`; unknown avg `18.642` n `1262`
- 4h: commodity avg `0.2369` n `13`; crypto_alt avg `-0.6066` n `239`; crypto_major avg `-0.8634` n `8`; equity avg `-0.9926` n `162`; fx avg `-0.0375` n `6`; index avg `-0.0672` n `27`; metal avg `-0.1143` n `20`; unknown avg `-0.2173` n `1170`
- 24h: commodity avg `-0.8005` n `13`; crypto_alt avg `0.9446` n `239`; crypto_major avg `1.2117` n `8`; equity avg `-2.9771` n `162`; fx avg `-0.0757` n `6`; index avg `-0.3321` n `27`; metal avg `-0.1526` n `20`; unknown avg `16.9129` n `1113`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
