# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T05:22:24.566557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.9308` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.8044` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.6443` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0665` n `12`; crypto_alt avg `-0.3592` n `228`; crypto_major avg `-0.4113` n `8`; equity avg `-0.1497` n `73`; fx avg `-0.0001` n `6`; index avg `-0.0505` n `23`; metal avg `-0.1062` n `18`; unknown avg `-0.1818` n `420`
- 1h: commodity avg `0.0528` n `12`; crypto_alt avg `-2.3075` n `228`; crypto_major avg `-1.942` n `8`; equity avg `-0.2977` n `73`; fx avg `-0.0054` n `6`; index avg `-0.0112` n `23`; metal avg `-0.1376` n `18`; unknown avg `-0.4557` n `420`
- 4h: commodity avg `0.0094` n `12`; crypto_alt avg `-1.8353` n `228`; crypto_major avg `0.2433` n `8`; equity avg `0.1568` n `73`; fx avg `0.0041` n `6`; index avg `-0.0492` n `23`; metal avg `-0.161` n `18`; unknown avg `0.1083` n `420`
- 24h: commodity avg `0.1488` n `12`; crypto_alt avg `-4.7221` n `228`; crypto_major avg `-3.9448` n `8`; equity avg `-3.7897` n `73`; fx avg `-0.0106` n `6`; index avg `-1.1633` n `23`; metal avg `-1.4996` n `18`; unknown avg `-0.2263` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
