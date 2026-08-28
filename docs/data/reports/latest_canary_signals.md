# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T16:22:27.109940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-2.3663` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `-2.1978` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.157` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.9101` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.7681` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-1.0971` n `231`; crypto_major avg `-1.0391` n `8`; equity avg `-0.3755` n `127`; fx avg `-0.0081` n `6`; index avg `-0.0994` n `26`; metal avg `-0.2717` n `20`; unknown avg `-0.2906` n `793`
- 1h: commodity avg `-0.0396` n `12`; crypto_alt avg `-2.6442` n `231`; crypto_major avg `-2.4059` n `8`; equity avg `-1.3136` n `127`; fx avg `-0.0054` n `6`; index avg `-0.2489` n `26`; metal avg `-0.6378` n `20`; unknown avg `3.1919` n `793`
- 4h: commodity avg `0.1073` n `12`; crypto_alt avg `-2.5505` n `231`; crypto_major avg `-2.0905` n `8`; equity avg `-1.5708` n `127`; fx avg `-0.0201` n `6`; index avg `-0.1804` n `26`; metal avg `-0.7184` n `20`; unknown avg `-0.6087` n `792`
- 24h: commodity avg `-0.0447` n `12`; crypto_alt avg `-4.2098` n `231`; crypto_major avg `-3.7568` n `8`; equity avg `-1.9618` n `127`; fx avg `-0.0854` n `6`; index avg `-0.1351` n `26`; metal avg `-0.1616` n `20`; unknown avg `-0.2225` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
