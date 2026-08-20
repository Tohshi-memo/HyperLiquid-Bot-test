# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T09:37:26.349402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.9925` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.6075` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.3061` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.0283` n `230`; crypto_major avg `-0.2325` n `8`; equity avg `-0.1048` n `121`; fx avg `0.0152` n `6`; index avg `-0.0131` n `25`; metal avg `-0.0308` n `20`; unknown avg `0.0349` n `792`
- 1h: commodity avg `0.0398` n `12`; crypto_alt avg `0.4297` n `230`; crypto_major avg `0.5894` n `8`; equity avg `0.245` n `121`; fx avg `0.0285` n `6`; index avg `0.0234` n `25`; metal avg `-0.0303` n `20`; unknown avg `0.0264` n `792`
- 4h: commodity avg `0.3116` n `12`; crypto_alt avg `1.9863` n `230`; crypto_major avg `2.6177` n `8`; equity avg `-0.3748` n `121`; fx avg `0.0387` n `6`; index avg `-0.082` n `25`; metal avg `0.0102` n `20`; unknown avg `5.951` n `776`
- 24h: commodity avg `0.2028` n `12`; crypto_alt avg `7.575` n `230`; crypto_major avg `12.6717` n `8`; equity avg `0.1424` n `120`; fx avg `0.1756` n `6`; index avg `0.0427` n `25`; metal avg `0.9373` n `20`; unknown avg `2.2227` n `775`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
