# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T18:37:29.526210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5421` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `-0.203` n `234`; crypto_major avg `-0.0509` n `8`; equity avg `-0.02` n `140`; fx avg `-0.0021` n `6`; index avg `0.0005` n `26`; metal avg `-0.0075` n `20`; unknown avg `0.1978` n `935`
- 1h: commodity avg `-0.0203` n `12`; crypto_alt avg `-0.2158` n `234`; crypto_major avg `0.0211` n `8`; equity avg `-0.0374` n `140`; fx avg `0.0121` n `6`; index avg `0.0031` n `26`; metal avg `-0.0154` n `20`; unknown avg `33.4076` n `933`
- 4h: commodity avg `-0.0109` n `12`; crypto_alt avg `2.514` n `234`; crypto_major avg `1.5283` n `8`; equity avg `0.2721` n `140`; fx avg `0.0274` n `6`; index avg `0.04` n `26`; metal avg `-0.0138` n `20`; unknown avg `0.8638` n `871`
- 24h: commodity avg `0.3542` n `12`; crypto_alt avg `0.0993` n `234`; crypto_major avg `-0.737` n `8`; equity avg `-0.0939` n `140`; fx avg `-0.0279` n `6`; index avg `-0.0399` n `26`; metal avg `-0.0438` n `20`; unknown avg `61.9494` n `819`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
