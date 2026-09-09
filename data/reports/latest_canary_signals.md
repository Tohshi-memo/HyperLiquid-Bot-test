# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T23:21:58.844451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6707` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6684` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `0.1749` n `233`; crypto_major avg `0.1179` n `8`; equity avg `-0.0144` n `134`; fx avg `0.0068` n `6`; index avg `-0.0057` n `26`; metal avg `-0.0018` n `20`; unknown avg `1.696` n `797`
- 1h: commodity avg `0.0319` n `12`; crypto_alt avg `0.4073` n `233`; crypto_major avg `0.0805` n `8`; equity avg `0.0023` n `134`; fx avg `0.0003` n `6`; index avg `-0.0023` n `26`; metal avg `0.0267` n `20`; unknown avg `0.29` n `785`
- 4h: commodity avg `0.1282` n `12`; crypto_alt avg `-2.5765` n `233`; crypto_major avg `-1.702` n `8`; equity avg `-0.5083` n `134`; fx avg `-0.0078` n `6`; index avg `-0.0313` n `26`; metal avg `-0.0336` n `20`; unknown avg `21.2026` n `691`
- 24h: commodity avg `0.1533` n `12`; crypto_alt avg `-2.9803` n `233`; crypto_major avg `-1.9754` n `8`; equity avg `-0.6378` n `134`; fx avg `0.0019` n `6`; index avg `-0.1353` n `26`; metal avg `0.5718` n `20`; unknown avg `1.0696` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
