# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T14:22:31.322296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0607` n `12`; crypto_alt avg `-0.2712` n `229`; crypto_major avg `-0.3165` n `8`; equity avg `-0.9541` n `91`; fx avg `-0.0047` n `6`; index avg `-0.1545` n `25`; metal avg `-0.1732` n `20`; unknown avg `-0.064` n `765`
- 1h: commodity avg `-0.2428` n `12`; crypto_alt avg `0.0532` n `229`; crypto_major avg `-0.0982` n `8`; equity avg `-0.3292` n `91`; fx avg `0.0` n `6`; index avg `-0.0424` n `25`; metal avg `-0.0088` n `20`; unknown avg `0.1777` n `765`
- 4h: commodity avg `-0.4814` n `12`; crypto_alt avg `-0.0578` n `229`; crypto_major avg `-0.3593` n `8`; equity avg `0.1159` n `91`; fx avg `-0.0187` n `6`; index avg `0.1323` n `25`; metal avg `0.255` n `20`; unknown avg `0.1972` n `764`
- 24h: commodity avg `-0.8961` n `12`; crypto_alt avg `1.0605` n `229`; crypto_major avg `0.3076` n `8`; equity avg `1.4999` n `91`; fx avg `0.0851` n `6`; index avg `0.278` n `25`; metal avg `0.7669` n `20`; unknown avg `0.8964` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
