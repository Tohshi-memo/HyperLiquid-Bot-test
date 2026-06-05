# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T14:37:31.823945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.63` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1112` n `12`; crypto_alt avg `0.3516` n `228`; crypto_major avg `0.5622` n `8`; equity avg `0.2995` n `74`; fx avg `-0.0346` n `6`; index avg `0.1321` n `23`; metal avg `-0.0284` n `18`; unknown avg `-0.0427` n `424`
- 1h: commodity avg `-0.1709` n `12`; crypto_alt avg `-0.9511` n `228`; crypto_major avg `-1.1189` n `8`; equity avg `-0.6083` n `74`; fx avg `-0.109` n `6`; index avg `-0.4429` n `23`; metal avg `-0.9955` n `18`; unknown avg `-0.4938` n `424`
- 4h: commodity avg `-0.6132` n `12`; crypto_alt avg `-0.9723` n `228`; crypto_major avg `-0.858` n `8`; equity avg `-2.2018` n `74`; fx avg `-0.1289` n `6`; index avg `-1.3736` n `23`; metal avg `-2.488` n `18`; unknown avg `1.2496` n `424`
- 24h: commodity avg `-0.7245` n `12`; crypto_alt avg `-6.0831` n `228`; crypto_major avg `-4.6993` n `8`; equity avg `-3.2277` n `74`; fx avg `-0.012` n `6`; index avg `-1.5796` n `23`; metal avg `-3.117` n `18`; unknown avg `-0.4891` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
