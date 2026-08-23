# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T05:37:29.601765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.1688` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1482` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.1309` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.0071` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.0689` n `230`; crypto_major avg `-0.0905` n `8`; equity avg `-0.0287` n `121`; fx avg `-0.0263` n `6`; index avg `-0.0102` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.2646` n `794`
- 1h: commodity avg `-0.0215` n `12`; crypto_alt avg `-0.1603` n `230`; crypto_major avg `-0.3504` n `8`; equity avg `-0.1092` n `121`; fx avg `-0.0165` n `6`; index avg `-0.011` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.3283` n `794`
- 4h: commodity avg `-0.0335` n `12`; crypto_alt avg `-2.6813` n `230`; crypto_major avg `-2.1644` n `8`; equity avg `-0.1573` n `121`; fx avg `0.007` n `6`; index avg `0.0044` n `25`; metal avg `-0.0162` n `20`; unknown avg `3.6761` n `794`
- 24h: commodity avg `-0.0617` n `12`; crypto_alt avg `-4.1046` n `230`; crypto_major avg `-1.5773` n `8`; equity avg `0.0389` n `121`; fx avg `0.0741` n `6`; index avg `-0.0104` n `25`; metal avg `0.0719` n `20`; unknown avg `2.2977` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
