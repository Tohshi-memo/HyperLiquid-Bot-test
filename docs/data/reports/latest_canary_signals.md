# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T10:44:49.155017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6671` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.59` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `1.4709` n `230`; crypto_major avg `1.455` n `8`; equity avg `0.0984` n `121`; fx avg `0.0081` n `6`; index avg `0.0014` n `25`; metal avg `0.0136` n `20`; unknown avg `0.4059` n `794`
- 1h: commodity avg `-0.0145` n `12`; crypto_alt avg `-0.829` n `230`; crypto_major avg `-0.6301` n `8`; equity avg `-0.0845` n `121`; fx avg `0.0157` n `6`; index avg `-0.0098` n `25`; metal avg `0.006` n `20`; unknown avg `0.0779` n `794`
- 4h: commodity avg `-0.024` n `12`; crypto_alt avg `-1.2126` n `230`; crypto_major avg `-1.6157` n `8`; equity avg `-0.1269` n `121`; fx avg `0.0117` n `6`; index avg `-0.0257` n `25`; metal avg `0.0514` n `20`; unknown avg `0.7412` n `794`
- 24h: commodity avg `0.0288` n `12`; crypto_alt avg `2.3216` n `230`; crypto_major avg `3.2262` n `8`; equity avg `-0.9914` n `121`; fx avg `0.0445` n `6`; index avg `-0.1074` n `25`; metal avg `-0.1066` n `20`; unknown avg `1.5764` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
