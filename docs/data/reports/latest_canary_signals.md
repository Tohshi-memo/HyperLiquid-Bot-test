# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T11:22:27.303773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.3908` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.3621` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.3562` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.1247` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.2867` n `230`; crypto_major avg `-0.2656` n `8`; equity avg `-0.008` n `121`; fx avg `0.0061` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.02` n `794`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `1.0062` n `230`; crypto_major avg `0.8948` n `8`; equity avg `0.0307` n `121`; fx avg `0.0176` n `6`; index avg `0.0055` n `25`; metal avg `-0.0141` n `20`; unknown avg `0.3053` n `794`
- 4h: commodity avg `-0.0319` n `12`; crypto_alt avg `-2.2402` n `230`; crypto_major avg `-2.3881` n `8`; equity avg `-0.2634` n `121`; fx avg `0.0285` n `6`; index avg `-0.026` n `25`; metal avg `0.0027` n `20`; unknown avg `0.0424` n `794`
- 24h: commodity avg `-0.0548` n `12`; crypto_alt avg `1.1894` n `230`; crypto_major avg `2.4817` n `8`; equity avg `-1.0562` n `121`; fx avg `0.0651` n `6`; index avg `-0.1197` n `25`; metal avg `-0.2473` n `20`; unknown avg `1.3561` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
