# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T05:22:25.303630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-4.4885` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `4.4189` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-4.3204` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-3.8013` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.237` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `-0.8418` n `230`; crypto_major avg `-1.3923` n `8`; equity avg `0.0961` n `121`; fx avg `-0.002` n `6`; index avg `0.0424` n `25`; metal avg `0.1003` n `20`; unknown avg `0.6649` n `794`
- 1h: commodity avg `0.0351` n `12`; crypto_alt avg `-5.6488` n `230`; crypto_major avg `-4.4534` n `8`; equity avg `-0.6521` n `121`; fx avg `-0.0079` n `6`; index avg `-0.0345` n `25`; metal avg `-0.133` n `20`; unknown avg `8.3435` n `794`
- 4h: commodity avg `0.048` n `12`; crypto_alt avg `-2.5067` n `230`; crypto_major avg `-1.2817` n `8`; equity avg `-0.6355` n `121`; fx avg `0.0276` n `6`; index avg `-0.0447` n `25`; metal avg `-0.1701` n `20`; unknown avg `1.0378` n `793`
- 24h: commodity avg `0.2003` n `12`; crypto_alt avg `5.2113` n `230`; crypto_major avg `4.3658` n `8`; equity avg `-0.5039` n `121`; fx avg `0.0557` n `6`; index avg `-0.0788` n `25`; metal avg `0.0838` n `20`; unknown avg `1.766` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
