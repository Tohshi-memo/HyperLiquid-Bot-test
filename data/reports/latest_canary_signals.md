# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T22:52:25.895504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0709` n `13`; crypto_alt avg `-0.1546` n `239`; crypto_major avg `0.0033` n `8`; equity avg `-0.0679` n `162`; fx avg `-0.0076` n `6`; index avg `0.0055` n `27`; metal avg `-0.0067` n `20`; unknown avg `-0.1666` n `1236`
- 1h: commodity avg `0.0234` n `13`; crypto_alt avg `-0.3632` n `239`; crypto_major avg `-0.1855` n `8`; equity avg `-0.167` n `162`; fx avg `0.0114` n `6`; index avg `0.0038` n `27`; metal avg `0.005` n `20`; unknown avg `5.7704` n `1226`
- 4h: commodity avg `-0.1284` n `13`; crypto_alt avg `-0.117` n `239`; crypto_major avg `0.602` n `8`; equity avg `-0.528` n `162`; fx avg `0.0084` n `6`; index avg `-0.0752` n `27`; metal avg `-0.0188` n `20`; unknown avg `4.8664` n `1188`
- 24h: commodity avg `-1.2064` n `13`; crypto_alt avg `-0.3005` n `239`; crypto_major avg `0.2556` n `8`; equity avg `-3.5258` n `162`; fx avg `-0.1192` n `6`; index avg `-0.3393` n `27`; metal avg `-0.3804` n `20`; unknown avg `516.8242` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
