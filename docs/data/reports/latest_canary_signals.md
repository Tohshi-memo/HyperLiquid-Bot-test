# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T18:52:27.925170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5146` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.469` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `-0.3468` n `230`; crypto_major avg `-0.4384` n `8`; equity avg `-0.0371` n `102`; fx avg `0.0106` n `6`; index avg `-0.0038` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.0804` n `782`
- 1h: commodity avg `-0.0392` n `12`; crypto_alt avg `-0.8336` n `230`; crypto_major avg `-0.8688` n `8`; equity avg `-0.1603` n `102`; fx avg `0.003` n `6`; index avg `-0.0166` n `25`; metal avg `-0.009` n `20`; unknown avg `1.7622` n `782`
- 4h: commodity avg `0.1067` n `12`; crypto_alt avg `-1.4514` n `230`; crypto_major avg `-1.5258` n `8`; equity avg `-0.3499` n `102`; fx avg `-0.0016` n `6`; index avg `-0.0568` n `25`; metal avg `-0.0112` n `20`; unknown avg `2.1565` n `782`
- 24h: commodity avg `0.6105` n `12`; crypto_alt avg `-1.3824` n `230`; crypto_major avg `-2.0548` n `8`; equity avg `-1.4221` n `102`; fx avg `-0.147` n `6`; index avg `-0.1847` n `25`; metal avg `-0.1182` n `20`; unknown avg `4.1973` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
