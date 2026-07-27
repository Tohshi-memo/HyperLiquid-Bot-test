# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T23:37:39.052197+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.831` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7935` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.506` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0239` n `12`; crypto_alt avg `-0.2645` n `230`; crypto_major avg `-0.1639` n `8`; equity avg `0.0829` n `102`; fx avg `0.0048` n `6`; index avg `0.0058` n `25`; metal avg `0.0154` n `20`; unknown avg `-0.0764` n `774`
- 1h: commodity avg `0.0511` n `12`; crypto_alt avg `-1.3443` n `230`; crypto_major avg `-0.9782` n `8`; equity avg `-0.1788` n `102`; fx avg `0.002` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0076` n `20`; unknown avg `-0.1983` n `774`
- 4h: commodity avg `-0.0219` n `12`; crypto_alt avg `-1.8911` n `230`; crypto_major avg `-1.8786` n `8`; equity avg `-0.3726` n `102`; fx avg `-0.0138` n `6`; index avg `-0.0476` n `25`; metal avg `-0.0851` n `20`; unknown avg `-0.155` n `774`
- 24h: commodity avg `-0.6583` n `12`; crypto_alt avg `-3.7123` n `230`; crypto_major avg `-3.0532` n `8`; equity avg `-1.9854` n `102`; fx avg `-0.0319` n `6`; index avg `-0.5117` n `25`; metal avg `0.01` n `20`; unknown avg `1161.737` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3584`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.3063`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1928`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
