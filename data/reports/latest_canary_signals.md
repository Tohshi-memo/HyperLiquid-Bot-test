# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T18:37:47.749861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `4.035` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `4.0164` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.7867` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1089` n `12`; crypto_alt avg `0.0966` n `230`; crypto_major avg `0.1839` n `8`; equity avg `0.0573` n `121`; fx avg `0.0071` n `6`; index avg `0.041` n `25`; metal avg `0.0302` n `20`; unknown avg `-0.0283` n `792`
- 1h: commodity avg `-0.2489` n `12`; crypto_alt avg `0.1203` n `230`; crypto_major avg `0.4934` n `8`; equity avg `-0.0908` n `121`; fx avg `0.0007` n `6`; index avg `0.0162` n `25`; metal avg `-0.016` n `20`; unknown avg `1.1319` n `792`
- 4h: commodity avg `-0.1782` n `12`; crypto_alt avg `2.097` n `230`; crypto_major avg `3.8382` n `8`; equity avg `-0.1968` n `121`; fx avg `0.0167` n `6`; index avg `-0.0584` n `25`; metal avg `0.0515` n `20`; unknown avg `0.0956` n `792`
- 24h: commodity avg `0.0624` n `12`; crypto_alt avg `2.6636` n `230`; crypto_major avg `4.778` n `8`; equity avg `-0.6607` n `120`; fx avg `-0.2066` n `6`; index avg `-0.0188` n `25`; metal avg `0.7852` n `20`; unknown avg `0.4272` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
