# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T17:37:46.935501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.8424` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5205` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.1395` n `231`; crypto_major avg `-0.3436` n `8`; equity avg `-0.0623` n `127`; fx avg `0.0055` n `6`; index avg `-0.0207` n `26`; metal avg `0.0182` n `20`; unknown avg `0.0746` n `792`
- 1h: commodity avg `0.073` n `12`; crypto_alt avg `-0.1725` n `231`; crypto_major avg `-0.0484` n `8`; equity avg `0.1959` n `127`; fx avg `-0.007` n `6`; index avg `0.0182` n `26`; metal avg `0.0535` n `20`; unknown avg `0.1774` n `792`
- 4h: commodity avg `0.0247` n `12`; crypto_alt avg `1.4585` n `231`; crypto_major avg `1.9146` n `8`; equity avg `0.0722` n `127`; fx avg `-0.0405` n `6`; index avg `0.0734` n `26`; metal avg `0.3941` n `20`; unknown avg `0.2718` n `792`
- 24h: commodity avg `0.1539` n `12`; crypto_alt avg `3.703` n `231`; crypto_major avg `4.1016` n `8`; equity avg `1.6086` n `127`; fx avg `-0.0615` n `6`; index avg `0.2051` n `26`; metal avg `0.2185` n `20`; unknown avg `0.9442` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
