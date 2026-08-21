# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T10:19:00.825633+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1329` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.0653` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.5624` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.3993` n `230`; crypto_major avg `0.4119` n `8`; equity avg `-0.0195` n `121`; fx avg `0.0003` n `6`; index avg `-0.0176` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.0089` n `793`
- 1h: commodity avg `0.1646` n `12`; crypto_alt avg `1.545` n `230`; crypto_major avg `1.2081` n `8`; equity avg `0.2196` n `121`; fx avg `0.0055` n `6`; index avg `0.0122` n `25`; metal avg `-0.1227` n `20`; unknown avg `0.1896` n `793`
- 4h: commodity avg `0.2222` n `12`; crypto_alt avg `2.6131` n `230`; crypto_major avg `2.2875` n `8`; equity avg `0.7251` n `121`; fx avg `-0.0177` n `6`; index avg `0.0232` n `25`; metal avg `0.1546` n `20`; unknown avg `0.4885` n `793`
- 24h: commodity avg `0.2111` n `12`; crypto_alt avg `7.1034` n `230`; crypto_major avg `7.1468` n `8`; equity avg `0.4752` n `121`; fx avg `-0.0793` n `6`; index avg `-0.0143` n `25`; metal avg `0.8067` n `20`; unknown avg `2.5573` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2206`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1895`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
