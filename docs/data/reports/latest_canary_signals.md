# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T20:52:24.494521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9526` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.382` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.3685` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.763` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `1.0034` n `230`; crypto_major avg `1.3492` n `8`; equity avg `0.1181` n `121`; fx avg `-0.0038` n `6`; index avg `0.0278` n `25`; metal avg `0.0183` n `20`; unknown avg `0.1049` n `792`
- 1h: commodity avg `0.0202` n `12`; crypto_alt avg `1.1938` n `230`; crypto_major avg `1.8276` n `8`; equity avg `0.3809` n `121`; fx avg `-0.0078` n `6`; index avg `0.0437` n `25`; metal avg `0.0646` n `20`; unknown avg `0.9717` n `792`
- 4h: commodity avg `-0.3854` n `12`; crypto_alt avg `1.6867` n `230`; crypto_major avg `3.5672` n `8`; equity avg `0.1987` n `121`; fx avg `-0.0063` n `6`; index avg `-0.0149` n `25`; metal avg `0.1852` n `20`; unknown avg `1.957` n `792`
- 24h: commodity avg `-0.1037` n `12`; crypto_alt avg `5.1577` n `230`; crypto_major avg `8.8679` n `8`; equity avg `0.3216` n `120`; fx avg `-0.2029` n `6`; index avg `0.0575` n `25`; metal avg `1.2226` n `20`; unknown avg `1.1181` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1977`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
