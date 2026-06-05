# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T21:52:22.305808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.8002` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.768` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0431` n `12`; crypto_alt avg `0.2249` n `228`; crypto_major avg `0.1006` n `8`; equity avg `0.0383` n `74`; fx avg `-0.0084` n `6`; index avg `-0.0365` n `23`; metal avg `0.0312` n `18`; unknown avg `0.3035` n `425`
- 1h: commodity avg `-0.1597` n `12`; crypto_alt avg `0.8657` n `228`; crypto_major avg `0.678` n `8`; equity avg `0.4273` n `74`; fx avg `0.0036` n `6`; index avg `0.2928` n `23`; metal avg `0.1078` n `18`; unknown avg `0.5307` n `425`
- 4h: commodity avg `-0.1362` n `12`; crypto_alt avg `1.1798` n `228`; crypto_major avg `1.231` n `8`; equity avg `-0.5692` n `74`; fx avg `-0.0114` n `6`; index avg `-0.9601` n `23`; metal avg `-0.537` n `18`; unknown avg `1.0032` n `424`
- 24h: commodity avg `-1.8275` n `12`; crypto_alt avg `-4.7831` n `228`; crypto_major avg `-4.1939` n `8`; equity avg `-5.9685` n `74`; fx avg `-0.0522` n `6`; index avg `-4.3974` n `23`; metal avg `-4.4085` n `18`; unknown avg `-1.5579` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
