# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T05:07:26.559548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0498` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0473` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0358` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8571` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.1539` n `239`; crypto_major avg `-0.0951` n `8`; equity avg `0.0083` n `162`; fx avg `0.0037` n `6`; index avg `0.0003` n `27`; metal avg `-0.0023` n `20`; unknown avg `2.3542` n `1256`
- 1h: commodity avg `0.0063` n `13`; crypto_alt avg `0.0732` n `239`; crypto_major avg `0.2428` n `8`; equity avg `0.0047` n `162`; fx avg `0.0052` n `6`; index avg `0.0026` n `27`; metal avg `0.0185` n `20`; unknown avg `2.5749` n `1254`
- 4h: commodity avg `-0.048` n `13`; crypto_alt avg `-1.549` n `239`; crypto_major avg `-2.0978` n `8`; equity avg `-0.2407` n `162`; fx avg `0.0026` n `6`; index avg `-0.0505` n `27`; metal avg `-0.062` n `20`; unknown avg `5.148` n `1242`
- 24h: commodity avg `-0.0934` n `13`; crypto_alt avg `-0.0595` n `239`; crypto_major avg `-1.6611` n `8`; equity avg `-2.7227` n `162`; fx avg `-0.0896` n `6`; index avg `-0.2354` n `27`; metal avg `-0.5912` n `20`; unknown avg `60.6327` n `1026`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
