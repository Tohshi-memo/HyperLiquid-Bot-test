# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T16:52:29.624688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.3696` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.1625` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.788` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `-0.4251` n `228`; crypto_major avg `-0.3738` n `8`; equity avg `-0.0722` n `86`; fx avg `-0.0043` n `6`; index avg `-0.0186` n `23`; metal avg `-0.0036` n `20`; unknown avg `0.0264` n `765`
- 1h: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.4917` n `228`; crypto_major avg `-0.3777` n `8`; equity avg `-0.041` n `86`; fx avg `0.008` n `6`; index avg `-0.0028` n `23`; metal avg `-0.1534` n `20`; unknown avg `0.2328` n `765`
- 4h: commodity avg `0.278` n `12`; crypto_alt avg `-2.5047` n `228`; crypto_major avg `-3.0916` n `8`; equity avg `-2.6817` n `86`; fx avg `0.0679` n `6`; index avg `-0.3036` n `23`; metal avg `0.0709` n `20`; unknown avg `1.2203` n `765`
- 24h: commodity avg `0.2669` n `12`; crypto_alt avg `-0.0541` n `228`; crypto_major avg `-0.6718` n `8`; equity avg `-0.529` n `86`; fx avg `0.0754` n `6`; index avg `0.3265` n `23`; metal avg `0.2504` n `20`; unknown avg `0.4795` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
