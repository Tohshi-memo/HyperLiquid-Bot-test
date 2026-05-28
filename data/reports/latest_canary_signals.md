# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T06:52:19.784976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.339` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1553` n `12`; crypto_alt avg `0.4783` n `228`; crypto_major avg `0.4077` n `8`; equity avg `0.0069` n `67`; fx avg `0.0147` n `6`; index avg `0.114` n `23`; metal avg `0.1364` n `18`; unknown avg `0.9867` n `419`
- 1h: commodity avg `-0.2873` n `12`; crypto_alt avg `0.2328` n `228`; crypto_major avg `0.1586` n `8`; equity avg `0.1239` n `67`; fx avg `0.0166` n `6`; index avg `0.1602` n `23`; metal avg `0.0262` n `18`; unknown avg `1.0115` n `409`
- 4h: commodity avg `-0.0218` n `12`; crypto_alt avg `-2.6078` n `228`; crypto_major avg `-1.4791` n `8`; equity avg `-0.4177` n `67`; fx avg `-0.0688` n `6`; index avg `-0.1401` n `23`; metal avg `-0.0132` n `18`; unknown avg `0.1628` n `409`
- 24h: commodity avg `0.1207` n `12`; crypto_alt avg `-5.1591` n `228`; crypto_major avg `-3.8434` n `8`; equity avg `-1.2213` n `67`; fx avg `-0.1278` n `6`; index avg `-0.8031` n `23`; metal avg `-1.5325` n `18`; unknown avg `-1.8337` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
