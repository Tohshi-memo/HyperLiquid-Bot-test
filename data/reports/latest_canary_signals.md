# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T01:07:27.386296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6559` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6291` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1599` n `12`; crypto_alt avg `-0.4718` n `231`; crypto_major avg `-0.4995` n `8`; equity avg `-0.3534` n `128`; fx avg `-0.013` n `6`; index avg `-0.0774` n `26`; metal avg `-0.1836` n `20`; unknown avg `-0.3216` n `791`
- 1h: commodity avg `0.113` n `12`; crypto_alt avg `0.3708` n `231`; crypto_major avg `0.095` n `8`; equity avg `0.2185` n `128`; fx avg `-0.0138` n `6`; index avg `0.0624` n `26`; metal avg `-0.1097` n `20`; unknown avg `0.0382` n `791`
- 4h: commodity avg `-0.1914` n `12`; crypto_alt avg `-1.6978` n `231`; crypto_major avg `-1.9228` n `8`; equity avg `-1.1807` n `128`; fx avg `-0.0019` n `6`; index avg `-0.2937` n `26`; metal avg `-0.2669` n `20`; unknown avg `3.2148` n `791`
- 24h: commodity avg `0.2884` n `12`; crypto_alt avg `-1.0256` n `231`; crypto_major avg `-2.1293` n `8`; equity avg `-1.2024` n `128`; fx avg `0.0154` n `6`; index avg `-0.3054` n `26`; metal avg `-0.2362` n `20`; unknown avg `-0.3937` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.048`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0435`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
