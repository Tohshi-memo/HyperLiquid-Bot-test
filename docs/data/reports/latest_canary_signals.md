# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T19:31:59.237234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0064` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `0.0875` n `230`; crypto_major avg `0.0981` n `8`; equity avg `-0.032` n `94`; fx avg `-0.0026` n `6`; index avg `-0.0284` n `25`; metal avg `-0.0485` n `20`; unknown avg `0.1228` n `768`
- 1h: commodity avg `0.0694` n `12`; crypto_alt avg `0.0309` n `230`; crypto_major avg `0.1841` n `8`; equity avg `-0.2696` n `94`; fx avg `0.0104` n `6`; index avg `-0.0982` n `25`; metal avg `0.0072` n `20`; unknown avg `-0.0209` n `768`
- 4h: commodity avg `0.0216` n `12`; crypto_alt avg `-0.8055` n `230`; crypto_major avg `-1.3088` n `8`; equity avg `-1.1465` n `94`; fx avg `-0.0279` n `6`; index avg `-0.3024` n `25`; metal avg `-0.4143` n `20`; unknown avg `-0.1835` n `768`
- 24h: commodity avg `-0.3949` n `12`; crypto_alt avg `-0.8434` n `230`; crypto_major avg `-1.8686` n `8`; equity avg `-3.7524` n `94`; fx avg `-0.1521` n `6`; index avg `-0.5701` n `25`; metal avg `-0.8151` n `20`; unknown avg `-0.406` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
