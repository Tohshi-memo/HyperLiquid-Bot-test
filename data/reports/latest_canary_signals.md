# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T14:07:29.771859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.22` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.6283` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0291` n `12`; crypto_alt avg `-0.3008` n `230`; crypto_major avg `-0.3354` n `8`; equity avg `0.0066` n `113`; fx avg `0.0144` n `6`; index avg `-0.0197` n `25`; metal avg `-0.0159` n `20`; unknown avg `0.078` n `786`
- 1h: commodity avg `0.0088` n `12`; crypto_alt avg `-0.4389` n `230`; crypto_major avg `-0.7359` n `8`; equity avg `0.1109` n `113`; fx avg `0.0298` n `6`; index avg `-0.0214` n `25`; metal avg `-0.0374` n `20`; unknown avg `0.4522` n `786`
- 4h: commodity avg `0.0062` n `12`; crypto_alt avg `-0.258` n `230`; crypto_major avg `-0.6692` n `8`; equity avg `0.9591` n `113`; fx avg `0.0264` n `6`; index avg `0.124` n `25`; metal avg `-0.0065` n `20`; unknown avg `0.0614` n `786`
- 24h: commodity avg `0.2345` n `12`; crypto_alt avg `-1.1033` n `230`; crypto_major avg `0.1778` n `8`; equity avg `2.6962` n `113`; fx avg `0.0615` n `6`; index avg `0.2949` n `25`; metal avg `0.3291` n `20`; unknown avg `-0.0553` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2359`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
