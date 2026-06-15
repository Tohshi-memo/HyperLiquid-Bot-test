# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T13:07:35.900116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.21` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.6074` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.083` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.0205` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.1074` n `12`; crypto_alt avg `0.172` n `228`; crypto_major avg `0.1836` n `8`; equity avg `-0.0178` n `74`; fx avg `-0.0021` n `6`; index avg `0.028` n `23`; metal avg `-0.0489` n `18`; unknown avg `-0.0161` n `689`
- 1h: commodity avg `-0.0412` n `12`; crypto_alt avg `0.3921` n `228`; crypto_major avg `0.6004` n `8`; equity avg `-0.1256` n `74`; fx avg `-0.0121` n `6`; index avg `-0.0164` n `23`; metal avg `0.0207` n `18`; unknown avg `-0.217` n `689`
- 4h: commodity avg `0.343` n `12`; crypto_alt avg `1.8334` n `228`; crypto_major avg `2.3635` n `8`; equity avg `-0.2439` n `74`; fx avg `0.001` n `6`; index avg `0.0593` n `23`; metal avg `0.2805` n `18`; unknown avg `0.2017` n `689`
- 24h: commodity avg `-1.1196` n `12`; crypto_alt avg `5.4018` n `228`; crypto_major avg `5.7621` n `8`; equity avg `1.5568` n `74`; fx avg `0.0267` n `6`; index avg `0.9114` n `23`; metal avg `2.7528` n `18`; unknown avg `1.3991` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
