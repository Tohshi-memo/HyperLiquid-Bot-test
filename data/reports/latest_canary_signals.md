# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T14:37:30.492588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.719` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.61` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.4013` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3913` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.2428` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1241` n `12`; crypto_alt avg `-0.2279` n `232`; crypto_major avg `-0.1575` n `8`; equity avg `0.064` n `133`; fx avg `-0.0098` n `6`; index avg `-0.0016` n `26`; metal avg `0.0262` n `20`; unknown avg `0.3764` n `793`
- 1h: commodity avg `0.2175` n `12`; crypto_alt avg `-0.2676` n `232`; crypto_major avg `-0.4496` n `8`; equity avg `0.4732` n `133`; fx avg `0.0351` n `6`; index avg `0.025` n `26`; metal avg `0.0827` n `20`; unknown avg `0.2513` n `785`
- 4h: commodity avg `0.032` n `12`; crypto_alt avg `-1.7904` n `232`; crypto_major avg `-2.3693` n `8`; equity avg `0.3497` n `133`; fx avg `-0.1244` n `6`; index avg `0.022` n `26`; metal avg `-0.1265` n `20`; unknown avg `0.1184` n `737`
- 24h: commodity avg `-0.3486` n `12`; crypto_alt avg `-0.1279` n `232`; crypto_major avg `-0.5038` n `8`; equity avg `2.4451` n `133`; fx avg `-0.0886` n `6`; index avg `0.3758` n `26`; metal avg `0.0269` n `20`; unknown avg `0.7943` n `698`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
