# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T14:27:32.005641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.6602` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.289` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.2746` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `2.2368` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.4453` n `234`; crypto_major avg `0.4661` n `8`; equity avg `0.2499` n `140`; fx avg `0.0225` n `6`; index avg `0.0139` n `26`; metal avg `0.017` n `20`; unknown avg `-0.0086` n `928`
- 1h: commodity avg `0.1147` n `12`; crypto_alt avg `0.8944` n `234`; crypto_major avg `2.0929` n `8`; equity avg `-0.1817` n `140`; fx avg `0.0332` n `6`; index avg `-0.0722` n `26`; metal avg `-0.1439` n `20`; unknown avg `1.8167` n `904`
- 4h: commodity avg `0.3915` n `12`; crypto_alt avg `0.686` n `234`; crypto_major avg `2.0466` n `8`; equity avg `-0.6136` n `140`; fx avg `-0.0084` n `6`; index avg `-0.1425` n `26`; metal avg `-0.2424` n `20`; unknown avg `1.9527` n `895`
- 24h: commodity avg `0.2215` n `12`; crypto_alt avg `5.6287` n `234`; crypto_major avg `5.4957` n `8`; equity avg `0.6071` n `140`; fx avg `0.2629` n `6`; index avg `-0.0885` n `26`; metal avg `-0.017` n `20`; unknown avg `3.9486` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
