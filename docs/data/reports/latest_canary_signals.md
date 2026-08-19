# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T19:52:31.604475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2516` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.0528` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7424` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.5008` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0307` n `12`; crypto_alt avg `0.168` n `230`; crypto_major avg `0.0895` n `8`; equity avg `-0.099` n `121`; fx avg `0.0084` n `6`; index avg `-0.0323` n `25`; metal avg `0.0296` n `20`; unknown avg `-0.0856` n `792`
- 1h: commodity avg `-0.0613` n `12`; crypto_alt avg `0.6674` n `230`; crypto_major avg `1.6069` n `8`; equity avg `0.2714` n `121`; fx avg `-0.0005` n `6`; index avg `-0.0358` n `25`; metal avg `0.1061` n `20`; unknown avg `0.4153` n `792`
- 4h: commodity avg `-0.3241` n `12`; crypto_alt avg `0.945` n `230`; crypto_major avg `1.9275` n `8`; equity avg `-0.1253` n `121`; fx avg `-0.0042` n `6`; index avg `-0.0836` n `25`; metal avg `0.1851` n `20`; unknown avg `0.363` n `792`
- 24h: commodity avg `-0.0579` n `12`; crypto_alt avg `3.6886` n `230`; crypto_major avg `6.6521` n `8`; equity avg `-0.2769` n `120`; fx avg `-0.1965` n `6`; index avg `-0.0418` n `25`; metal avg `1.1145` n `20`; unknown avg `0.8602` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
