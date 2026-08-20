# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T09:47:04.103108+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.9164` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.6585` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.4369` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.0629` n `230`; crypto_major avg `-0.0716` n `8`; equity avg `0.0681` n `121`; fx avg `0.0009` n `6`; index avg `0.0196` n `25`; metal avg `0.0155` n `20`; unknown avg `0.143` n `792`
- 1h: commodity avg `0.001` n `12`; crypto_alt avg `0.1904` n `230`; crypto_major avg `0.2471` n `8`; equity avg `0.2664` n `121`; fx avg `-0.002` n `6`; index avg `0.0516` n `25`; metal avg `0.0155` n `20`; unknown avg `0.1298` n `792`
- 4h: commodity avg `0.2573` n `12`; crypto_alt avg `2.089` n `230`; crypto_major avg `2.6942` n `8`; equity avg `-0.2222` n `121`; fx avg `0.0528` n `6`; index avg `-0.0383` n `25`; metal avg `0.0357` n `20`; unknown avg `0.6279` n `776`
- 24h: commodity avg `0.1748` n `12`; crypto_alt avg `7.5446` n `230`; crypto_major avg `12.6499` n `8`; equity avg `0.494` n `120`; fx avg `0.2248` n `6`; index avg `0.1021` n `25`; metal avg `0.9438` n `20`; unknown avg `2.3922` n `775`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
