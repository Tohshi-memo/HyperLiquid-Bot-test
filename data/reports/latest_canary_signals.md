# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T10:37:36.581772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5935` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.1354` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `0.066` n `230`; crypto_major avg `-0.137` n `8`; equity avg `-0.102` n `121`; fx avg `-0.0001` n `6`; index avg `-0.003` n `25`; metal avg `0.0958` n `20`; unknown avg `0.0215` n `792`
- 1h: commodity avg `-0.019` n `12`; crypto_alt avg `0.1878` n `230`; crypto_major avg `-0.0448` n `8`; equity avg `0.0706` n `121`; fx avg `0.0054` n `6`; index avg `0.0405` n `25`; metal avg `0.1119` n `20`; unknown avg `0.2047` n `792`
- 4h: commodity avg `0.2883` n `12`; crypto_alt avg `1.9099` n `230`; crypto_major avg `2.1585` n `8`; equity avg `-0.435` n `121`; fx avg `0.0988` n `6`; index avg `-0.0713` n `25`; metal avg `0.0231` n `20`; unknown avg `0.3071` n `792`
- 24h: commodity avg `0.1106` n `12`; crypto_alt avg `7.717` n `230`; crypto_major avg `12.6203` n `8`; equity avg `0.4728` n `120`; fx avg `0.2153` n `6`; index avg `0.1101` n `25`; metal avg `0.9803` n `20`; unknown avg `2.5947` n `775`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
