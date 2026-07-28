# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T14:07:30.697631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.1831` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.8223` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0087` n `12`; crypto_alt avg `0.1456` n `230`; crypto_major avg `0.1343` n `8`; equity avg `0.0481` n `102`; fx avg `-0.0123` n `6`; index avg `-0.0223` n `25`; metal avg `0.0985` n `20`; unknown avg `-0.0343` n `774`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `-0.4828` n `230`; crypto_major avg `-0.3838` n `8`; equity avg `-2.2061` n `102`; fx avg `0.01` n `6`; index avg `-0.1593` n `25`; metal avg `-0.0542` n `20`; unknown avg `0.0096` n `774`
- 4h: commodity avg `0.0661` n `12`; crypto_alt avg `-0.3766` n `230`; crypto_major avg `-0.2575` n `8`; equity avg `-2.4406` n `102`; fx avg `0.0338` n `6`; index avg `-0.1068` n `25`; metal avg `0.0884` n `20`; unknown avg `-0.0195` n `774`
- 24h: commodity avg `-0.714` n `12`; crypto_alt avg `-3.7322` n `230`; crypto_major avg `-3.8019` n `8`; equity avg `-4.864` n `102`; fx avg `-0.1345` n `6`; index avg `-0.6593` n `25`; metal avg `-0.4279` n `20`; unknown avg `1225.1474` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
