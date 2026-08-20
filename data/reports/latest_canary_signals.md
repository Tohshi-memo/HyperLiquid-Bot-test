# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T08:22:33.357903+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.4932` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.0167` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1035` n `12`; crypto_alt avg `0.6153` n `230`; crypto_major avg `0.5838` n `8`; equity avg `-0.1207` n `121`; fx avg `-0.0011` n `6`; index avg `-0.024` n `25`; metal avg `0.0493` n `20`; unknown avg `-0.01` n `792`
- 1h: commodity avg `0.0171` n `12`; crypto_alt avg `1.071` n `230`; crypto_major avg `1.0166` n `8`; equity avg `-0.3952` n `121`; fx avg `0.0122` n `6`; index avg `-0.0578` n `25`; metal avg `0.0953` n `20`; unknown avg `0.0463` n `792`
- 4h: commodity avg `0.1435` n `12`; crypto_alt avg `1.6196` n `230`; crypto_major avg `1.9793` n `8`; equity avg `-0.5139` n `121`; fx avg `0.0318` n `6`; index avg `-0.0898` n `25`; metal avg `-0.0374` n `20`; unknown avg `0.3742` n `776`
- 24h: commodity avg `0.1445` n `12`; crypto_alt avg `6.8148` n `230`; crypto_major avg `11.5379` n `8`; equity avg `-0.0539` n `120`; fx avg `0.13` n `6`; index avg `0.0565` n `25`; metal avg `1.0018` n `20`; unknown avg `2.0771` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
