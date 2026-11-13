# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T03:52:27.232384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.4072` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.0629` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.0162` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.7641` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-1.5889` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.4511` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0052` n `13`; crypto_alt avg `-0.896` n `239`; crypto_major avg `-0.7954` n `8`; equity avg `-0.2437` n `162`; fx avg `0.0019` n `6`; index avg `-0.0279` n `27`; metal avg `-0.0219` n `20`; unknown avg `3.7336` n `1262`
- 1h: commodity avg `-0.0378` n `13`; crypto_alt avg `-1.508` n `239`; crypto_major avg `-1.5631` n `8`; equity avg `-0.788` n `162`; fx avg `0.0099` n `6`; index avg `-0.112` n `27`; metal avg `0.0258` n `20`; unknown avg `0.2212` n `1256`
- 4h: commodity avg `-0.1585` n `13`; crypto_alt avg `-2.739` n `239`; crypto_major avg `-3.1747` n `8`; equity avg `-1.4106` n `162`; fx avg `0.0006` n `6`; index avg `-0.1118` n `27`; metal avg `0.2325` n `20`; unknown avg `15.8404` n `1249`
- 24h: commodity avg `0.8044` n `13`; crypto_alt avg `-3.3294` n `239`; crypto_major avg `-4.5335` n `8`; equity avg `-1.4396` n `162`; fx avg `-0.0131` n `6`; index avg `-0.033` n `27`; metal avg `-0.4047` n `20`; unknown avg `96.568` n `1121`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
