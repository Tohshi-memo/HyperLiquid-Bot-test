# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T17:51:30.037168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4857` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.1927` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `3.1656` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `0.0533` n `230`; crypto_major avg `0.0843` n `8`; equity avg `0.163` n `121`; fx avg `0.0032` n `6`; index avg `0.0136` n `25`; metal avg `0.02` n `20`; unknown avg `0.123` n `792`
- 1h: commodity avg `0.0836` n `12`; crypto_alt avg `0.2032` n `230`; crypto_major avg `0.5656` n `8`; equity avg `-0.0328` n `121`; fx avg `0.0115` n `6`; index avg `-0.0463` n `25`; metal avg `0.0061` n `20`; unknown avg `0.5778` n `792`
- 4h: commodity avg `-0.0407` n `12`; crypto_alt avg `1.8941` n `230`; crypto_major avg `3.445` n `8`; equity avg `0.2523` n `121`; fx avg `0.0236` n `6`; index avg `0.0238` n `25`; metal avg `0.2794` n `20`; unknown avg `1.0813` n `792`
- 24h: commodity avg `0.0346` n `12`; crypto_alt avg `6.8807` n `230`; crypto_major avg `11.4568` n `8`; equity avg `-0.3371` n `121`; fx avg `0.1905` n `6`; index avg `-0.0061` n `25`; metal avg `0.3326` n `20`; unknown avg `3.6422` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
