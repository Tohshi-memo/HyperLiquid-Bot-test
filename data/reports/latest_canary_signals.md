# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T14:37:31.720021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5107` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `2.1573` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.095` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.9011` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0297` n `12`; crypto_alt avg `-0.0983` n `234`; crypto_major avg `0.0506` n `8`; equity avg `0.0209` n `140`; fx avg `0.002` n `6`; index avg `-0.0061` n `26`; metal avg `-0.0016` n `20`; unknown avg `-0.0451` n `926`
- 1h: commodity avg `0.0484` n `12`; crypto_alt avg `0.5581` n `234`; crypto_major avg `1.8492` n `8`; equity avg `-0.3081` n `140`; fx avg `0.0303` n `6`; index avg `-0.0779` n `26`; metal avg `-0.0519` n `20`; unknown avg `2.2063` n `902`
- 4h: commodity avg `0.4039` n `12`; crypto_alt avg `0.3957` n `234`; crypto_major avg `1.8411` n `8`; equity avg `-0.6696` n `140`; fx avg `0.0042` n `6`; index avg `-0.1724` n `26`; metal avg `-0.2539` n `20`; unknown avg `1.9089` n `893`
- 24h: commodity avg `0.2199` n `12`; crypto_alt avg `5.599` n `234`; crypto_major avg `5.4343` n `8`; equity avg `0.5258` n `140`; fx avg `0.2728` n `6`; index avg `-0.1071` n `26`; metal avg `-0.0045` n `20`; unknown avg `3.8391` n `729`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
