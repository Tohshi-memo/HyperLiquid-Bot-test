# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T17:22:26.304331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.0856` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7362` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0403` n `12`; crypto_alt avg `0.2125` n `231`; crypto_major avg `0.2687` n `8`; equity avg `0.086` n `127`; fx avg `-0.0087` n `6`; index avg `0.0114` n `26`; metal avg `0.0077` n `20`; unknown avg `-0.0216` n `792`
- 1h: commodity avg `0.1508` n `12`; crypto_alt avg `0.193` n `231`; crypto_major avg `0.3239` n `8`; equity avg `0.3181` n `127`; fx avg `-0.0069` n `6`; index avg `0.0712` n `26`; metal avg `0.0659` n `20`; unknown avg `0.1167` n `792`
- 4h: commodity avg `0.128` n `12`; crypto_alt avg `1.3634` n `231`; crypto_major avg `2.0467` n `8`; equity avg `-0.0389` n `127`; fx avg `-0.0439` n `6`; index avg `0.0353` n `26`; metal avg `0.3105` n `20`; unknown avg `0.2178` n `792`
- 24h: commodity avg `0.1544` n `12`; crypto_alt avg `4.0274` n `231`; crypto_major avg `4.9648` n `8`; equity avg `1.8026` n `127`; fx avg `-0.0635` n `6`; index avg `0.2343` n `26`; metal avg `0.1959` n `20`; unknown avg `1.0504` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
