# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T15:07:48.714187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.9596` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-2.7771` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.6751` - Index perps are stronger than crypto majors; possible risk-on canary.
- polymarket_volume_spike: score `2.67` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.5492` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0886` n `12`; crypto_alt avg `0.4181` n `232`; crypto_major avg `0.2443` n `8`; equity avg `0.1164` n `133`; fx avg `-0.0036` n `6`; index avg `0.0183` n `26`; metal avg `0.1123` n `20`; unknown avg `1.1866` n `791`
- 1h: commodity avg `0.2978` n `12`; crypto_alt avg `-0.5692` n `232`; crypto_major avg `-0.6441` n `8`; equity avg `-0.1809` n `133`; fx avg `0.0196` n `6`; index avg `-0.0374` n `26`; metal avg `0.1201` n `20`; unknown avg `1.4571` n `787`
- 4h: commodity avg `0.1109` n `12`; crypto_alt avg `-2.0898` n `232`; crypto_major avg `-2.6662` n `8`; equity avg `0.2934` n `133`; fx avg `-0.1056` n `6`; index avg `0.0089` n `26`; metal avg `-0.117` n `20`; unknown avg `0.354` n `737`
- 24h: commodity avg `-0.1827` n `12`; crypto_alt avg `-1.1762` n `232`; crypto_major avg `-2.0863` n `8`; equity avg `1.6377` n `133`; fx avg `-0.0858` n `6`; index avg `0.2095` n `26`; metal avg `-0.2796` n `20`; unknown avg `29.6778` n `698`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
