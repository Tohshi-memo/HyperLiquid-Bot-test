# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T16:07:31.505233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `13`; crypto_alt avg `0.0328` n `239`; crypto_major avg `-0.0601` n `8`; equity avg `0.1656` n `162`; fx avg `0.0103` n `6`; index avg `0.0283` n `27`; metal avg `-0.0399` n `20`; unknown avg `0.0313` n `1251`
- 1h: commodity avg `0.0838` n `13`; crypto_alt avg `0.1966` n `239`; crypto_major avg `0.1018` n `8`; equity avg `0.4265` n `162`; fx avg `-0.0042` n `6`; index avg `0.1012` n `27`; metal avg `-0.1096` n `20`; unknown avg `8.067` n `1239`
- 4h: commodity avg `-0.3152` n `13`; crypto_alt avg `0.3751` n `239`; crypto_major avg `0.3398` n `8`; equity avg `-0.4904` n `162`; fx avg `0.0153` n `6`; index avg `0.0289` n `27`; metal avg `-0.2594` n `20`; unknown avg `14.6498` n `1227`
- 24h: commodity avg `-0.7057` n `13`; crypto_alt avg `-0.0894` n `239`; crypto_major avg `-0.118` n `8`; equity avg `-1.7304` n `162`; fx avg `-0.0325` n `6`; index avg `-0.1108` n `27`; metal avg `-0.1784` n `20`; unknown avg `302.5379` n `1037`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
