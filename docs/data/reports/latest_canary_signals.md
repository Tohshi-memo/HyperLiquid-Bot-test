# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T20:37:27.132168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.63` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0336` n `12`; crypto_alt avg `-0.0391` n `230`; crypto_major avg `0.003` n `8`; equity avg `-0.0061` n `94`; fx avg `-0.0029` n `6`; index avg `-0.007` n `25`; metal avg `-0.0068` n `20`; unknown avg `0.0291` n `768`
- 1h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.247` n `230`; crypto_major avg `0.1561` n `8`; equity avg `0.0697` n `94`; fx avg `-0.0003` n `6`; index avg `0.0316` n `25`; metal avg `0.0343` n `20`; unknown avg `-0.0953` n `768`
- 4h: commodity avg `0.2271` n `12`; crypto_alt avg `0.5998` n `230`; crypto_major avg `0.448` n `8`; equity avg `1.4432` n `94`; fx avg `0.0494` n `6`; index avg `0.2898` n `25`; metal avg `0.5083` n `20`; unknown avg `-0.2088` n `768`
- 24h: commodity avg `0.0889` n `12`; crypto_alt avg `0.6961` n `230`; crypto_major avg `0.8952` n `8`; equity avg `-0.5148` n `93`; fx avg `0.205` n `6`; index avg `-0.1364` n `25`; metal avg `0.1633` n `20`; unknown avg `0.1412` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
