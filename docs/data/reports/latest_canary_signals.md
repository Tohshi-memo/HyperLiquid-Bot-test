# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T19:07:29.731123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.314` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.051` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0463` n `12`; crypto_alt avg `-0.5766` n `230`; crypto_major avg `-0.2505` n `8`; equity avg `0.0361` n `121`; fx avg `-0.0009` n `6`; index avg `0.0061` n `25`; metal avg `-0.0204` n `20`; unknown avg `1.0505` n `793`
- 1h: commodity avg `-0.0826` n `12`; crypto_alt avg `-1.5556` n `230`; crypto_major avg `-1.0436` n `8`; equity avg `0.0249` n `121`; fx avg `-0.0037` n `6`; index avg `0.0074` n `25`; metal avg `-0.0241` n `20`; unknown avg `1.2177` n `793`
- 4h: commodity avg `0.0753` n `12`; crypto_alt avg `-1.5629` n `230`; crypto_major avg `-1.3009` n `8`; equity avg `0.1382` n `121`; fx avg `0.04` n `6`; index avg `0.0131` n `25`; metal avg `0.0972` n `20`; unknown avg `1.2305` n `793`
- 24h: commodity avg `0.1095` n `12`; crypto_alt avg `6.278` n `230`; crypto_major avg `4.4918` n `8`; equity avg `1.2694` n `121`; fx avg `-0.0933` n `6`; index avg `0.1261` n `25`; metal avg `0.602` n `20`; unknown avg `2.2244` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1774`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
