# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T18:37:30.086151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.831` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9986` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8679` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5398` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.3833` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1267` n `12`; crypto_alt avg `-0.2147` n `232`; crypto_major avg `-0.4542` n `8`; equity avg `-0.1747` n `131`; fx avg `0.0011` n `6`; index avg `-0.0343` n `26`; metal avg `-0.0819` n `20`; unknown avg `1.763` n `793`
- 1h: commodity avg `0.1029` n `12`; crypto_alt avg `-1.2843` n `232`; crypto_major avg `-1.4639` n `8`; equity avg `-0.4` n `131`; fx avg `0.01` n `6`; index avg `-0.0806` n `26`; metal avg `-0.1898` n `20`; unknown avg `1.149` n `791`
- 4h: commodity avg `0.6349` n `12`; crypto_alt avg `-1.9255` n `232`; crypto_major avg `-2.1961` n `8`; equity avg `-0.6563` n `131`; fx avg `0.0009` n `6`; index avg `-0.1975` n `26`; metal avg `-0.3282` n `20`; unknown avg `-0.7118` n `790`
- 24h: commodity avg `0.7569` n `12`; crypto_alt avg `-1.2651` n `232`; crypto_major avg `-2.9815` n `8`; equity avg `-1.6868` n `130`; fx avg `0.0424` n `6`; index avg `-0.3043` n `26`; metal avg `-0.7502` n `20`; unknown avg `-0.0478` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0408`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0384`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0364`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0361`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0334`, n `668`, weak_sample_signal
