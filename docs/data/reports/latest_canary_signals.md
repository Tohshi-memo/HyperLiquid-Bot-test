# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T10:54:50.393954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1539` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.129` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.766` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0672` n `12`; crypto_alt avg `0.6458` n `230`; crypto_major avg `0.3529` n `8`; equity avg `0.0445` n `121`; fx avg `-0.0034` n `6`; index avg `0.0047` n `25`; metal avg `-0.0051` n `20`; unknown avg `0.0741` n `793`
- 1h: commodity avg `0.0812` n `12`; crypto_alt avg `0.6329` n `230`; crypto_major avg `-0.4118` n `8`; equity avg `0.0201` n `121`; fx avg `0.0062` n `6`; index avg `0.0048` n `25`; metal avg `-0.0096` n `20`; unknown avg `0.0706` n `793`
- 4h: commodity avg `0.1437` n `12`; crypto_alt avg `3.0292` n `230`; crypto_major avg `2.2727` n `8`; equity avg `0.5067` n `121`; fx avg `-0.0271` n `6`; index avg `0.0027` n `25`; metal avg `0.1188` n `20`; unknown avg `0.656` n `793`
- 24h: commodity avg `0.1679` n `12`; crypto_alt avg `7.3308` n `230`; crypto_major avg `6.9499` n `8`; equity avg `0.5208` n `121`; fx avg `-0.0802` n `6`; index avg `-0.0239` n `25`; metal avg `0.7553` n `20`; unknown avg `2.4993` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2235`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.191`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
