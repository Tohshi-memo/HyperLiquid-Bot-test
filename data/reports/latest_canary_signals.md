# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T01:07:25.712799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4308` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5652` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1032` n `12`; crypto_alt avg `-0.0522` n `234`; crypto_major avg `-0.0546` n `8`; equity avg `0.1556` n `140`; fx avg `0.0176` n `6`; index avg `0.0235` n `26`; metal avg `0.1394` n `20`; unknown avg `0.5068` n `941`
- 1h: commodity avg `-0.316` n `12`; crypto_alt avg `0.3463` n `234`; crypto_major avg `0.5779` n `8`; equity avg `0.3051` n `140`; fx avg `-0.0087` n `6`; index avg `0.0136` n `26`; metal avg `0.1183` n `20`; unknown avg `0.3338` n `941`
- 4h: commodity avg `-0.6793` n `12`; crypto_alt avg `1.3587` n `234`; crypto_major avg `1.7515` n `8`; equity avg `0.977` n `140`; fx avg `0.013` n `6`; index avg `0.1435` n `26`; metal avg `0.1863` n `20`; unknown avg `1.8347` n `889`
- 24h: commodity avg `-0.4351` n `12`; crypto_alt avg `1.4959` n `234`; crypto_major avg `1.6178` n `8`; equity avg `0.8694` n `140`; fx avg `0.0132` n `6`; index avg `0.1291` n `26`; metal avg `0.1474` n `20`; unknown avg `3.8092` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
