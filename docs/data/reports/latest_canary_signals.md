# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T18:37:29.488409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-1.85` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.7935` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `1.7932` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.619` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1251` n `12`; crypto_alt avg `-0.3065` n `230`; crypto_major avg `-0.6548` n `8`; equity avg `-0.13` n `121`; fx avg `0.0066` n `6`; index avg `-0.0117` n `25`; metal avg `0.0207` n `20`; unknown avg `0.1286` n `792`
- 1h: commodity avg `0.1074` n `12`; crypto_alt avg `-1.0523` n `230`; crypto_major avg `-1.8563` n `8`; equity avg `-0.2373` n `121`; fx avg `0.018` n `6`; index avg `-0.0628` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.472` n `792`
- 4h: commodity avg `0.1904` n `12`; crypto_alt avg `0.6772` n `230`; crypto_major avg `1.1157` n `8`; equity avg `-0.6775` n `121`; fx avg `0.0474` n `6`; index avg `-0.1289` n `25`; metal avg `0.1662` n `20`; unknown avg `1.8344` n `792`
- 24h: commodity avg `0.3572` n `12`; crypto_alt avg `5.6876` n `230`; crypto_major avg `9.0358` n `8`; equity avg `-0.5088` n `121`; fx avg `0.2163` n `6`; index avg `-0.0892` n `25`; metal avg `0.3243` n `20`; unknown avg `3.5694` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
