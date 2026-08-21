# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T11:52:26.484466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0278` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0767` n `12`; crypto_alt avg `0.199` n `230`; crypto_major avg `-0.1564` n `8`; equity avg `-0.0729` n `121`; fx avg `-0.0037` n `6`; index avg `-0.0123` n `23`; metal avg `-0.0444` n `18`; unknown avg `0.0071` n `774`
- 1h: commodity avg `-0.0717` n `12`; crypto_alt avg `-0.1022` n `230`; crypto_major avg `-0.9996` n `8`; equity avg `-0.0722` n `121`; fx avg `-0.0231` n `6`; index avg `0.0282` n `23`; metal avg `0.0941` n `18`; unknown avg `0.1951` n `774`
- 4h: commodity avg `0.0557` n `12`; crypto_alt avg `1.5897` n `230`; crypto_major avg `0.6783` n `8`; equity avg `0.1911` n `121`; fx avg `-0.0024` n `6`; index avg `-0.0145` n `23`; metal avg `0.1384` n `18`; unknown avg `0.559` n `774`
- 24h: commodity avg `-0.0279` n `12`; crypto_alt avg `6.9663` n `230`; crypto_major avg `5.5925` n `8`; equity avg `1.3125` n `121`; fx avg `-0.1154` n `6`; index avg `0.1847` n `23`; metal avg `1.1641` n `18`; unknown avg `2.2841` n `757`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
