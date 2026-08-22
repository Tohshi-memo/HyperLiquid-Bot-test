# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T07:44:04.400269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6733` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6253` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.0616` n `230`; crypto_major avg `0.1783` n `8`; equity avg `0.0081` n `121`; fx avg `-0.0075` n `6`; index avg `-0.0012` n `25`; metal avg `0.0193` n `20`; unknown avg `0.0066` n `794`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.5431` n `230`; crypto_major avg `0.4285` n `8`; equity avg `0.0776` n `121`; fx avg `-0.0149` n `6`; index avg `0.0032` n `25`; metal avg `0.0403` n `20`; unknown avg `0.7096` n `794`
- 4h: commodity avg `0.076` n `12`; crypto_alt avg `-3.3643` n `230`; crypto_major avg `-1.7227` n `8`; equity avg `-0.3829` n `121`; fx avg `-0.004` n `6`; index avg `-0.0494` n `25`; metal avg `-0.0974` n `20`; unknown avg `0.4744` n `778`
- 24h: commodity avg `0.0845` n `12`; crypto_alt avg `5.7999` n `230`; crypto_major avg `6.935` n `8`; equity avg `-0.6003` n `121`; fx avg `0.0302` n `6`; index avg `-0.1114` n `25`; metal avg `0.0031` n `20`; unknown avg `1.8016` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
