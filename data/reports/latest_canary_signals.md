# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T17:37:43.051492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.43` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.9916` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0953` n `13`; crypto_alt avg `-0.1531` n `237`; crypto_major avg `-0.1161` n `8`; equity avg `-0.0762` n `151`; fx avg `-0.0071` n `6`; index avg `0.0047` n `26`; metal avg `-0.0329` n `20`; unknown avg `24.3764` n `1233`
- 1h: commodity avg `0.1655` n `13`; crypto_alt avg `-0.2535` n `237`; crypto_major avg `-0.624` n `8`; equity avg `-0.5354` n `151`; fx avg `0.0061` n `6`; index avg `-0.0303` n `26`; metal avg `0.0117` n `20`; unknown avg `7.7201` n `1231`
- 4h: commodity avg `-0.089` n `13`; crypto_alt avg `-0.9487` n `237`; crypto_major avg `-0.8806` n `8`; equity avg `-2.8722` n `151`; fx avg `0.0133` n `6`; index avg `-0.2424` n `26`; metal avg `-0.1463` n `20`; unknown avg `1.3488` n `1083`
- 24h: commodity avg `0.5812` n `13`; crypto_alt avg `-5.0575` n `237`; crypto_major avg `-4.0313` n `8`; equity avg `-5.115` n `151`; fx avg `-0.1318` n `6`; index avg `-0.6025` n `26`; metal avg `-0.9419` n `20`; unknown avg `4.0522` n `908`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
