# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T16:07:42.647784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7236` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.7052` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.5594` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.0443` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.012` n `13`; crypto_alt avg `-0.5264` n `239`; crypto_major avg `-0.1593` n `8`; equity avg `-0.0671` n `162`; fx avg `0.0005` n `6`; index avg `-0.0076` n `27`; metal avg `0.0386` n `20`; unknown avg `1.9252` n `1250`
- 1h: commodity avg `-0.0062` n `13`; crypto_alt avg `-0.877` n `239`; crypto_major avg `-0.7744` n `8`; equity avg `-0.3015` n `162`; fx avg `0.0033` n `6`; index avg `-0.0319` n `27`; metal avg `-0.1216` n `20`; unknown avg `2.1231` n `1252`
- 4h: commodity avg `-0.0442` n `13`; crypto_alt avg `-2.9778` n `239`; crypto_major avg `-2.7678` n `8`; equity avg `-0.7235` n `162`; fx avg `0.0132` n `6`; index avg `-0.0626` n `27`; metal avg `-0.2084` n `20`; unknown avg `1.3342` n `1250`
- 24h: commodity avg `-0.1702` n `13`; crypto_alt avg `-6.1221` n `239`; crypto_major avg `-5.5683` n `8`; equity avg `-0.5404` n `162`; fx avg `-0.0741` n `6`; index avg `-0.0139` n `27`; metal avg `-0.3342` n `20`; unknown avg `2.9777` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
