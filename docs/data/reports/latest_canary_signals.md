# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T04:22:36.001697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `13`; crypto_alt avg `0.0902` n `239`; crypto_major avg `0.0456` n `8`; equity avg `-0.0981` n `162`; fx avg `-0.0181` n `6`; index avg `0.0022` n `27`; metal avg `0.0108` n `20`; unknown avg `1.1589` n `1260`
- 1h: commodity avg `-0.0884` n `13`; crypto_alt avg `0.3137` n `239`; crypto_major avg `0.4157` n `8`; equity avg `-0.412` n `162`; fx avg `-0.0388` n `6`; index avg `-0.0755` n `27`; metal avg `-0.1` n `20`; unknown avg `2.1225` n `1248`
- 4h: commodity avg `-0.2314` n `13`; crypto_alt avg `0.9431` n `239`; crypto_major avg `1.0734` n `8`; equity avg `0.3531` n `162`; fx avg `0.0112` n `6`; index avg `-0.0022` n `27`; metal avg `0.1986` n `20`; unknown avg `14.8128` n `1248`
- 24h: commodity avg `-1.2276` n `13`; crypto_alt avg `0.4371` n `239`; crypto_major avg `1.0147` n `8`; equity avg `-2.7855` n `162`; fx avg `-0.0525` n `6`; index avg `-0.3014` n `27`; metal avg `-0.0842` n `20`; unknown avg `560.2268` n `989`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
