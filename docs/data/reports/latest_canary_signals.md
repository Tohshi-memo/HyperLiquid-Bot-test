# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T13:22:21.059442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0945` n `12`; crypto_alt avg `-0.2025` n `228`; crypto_major avg `-0.0769` n `8`; equity avg `0.0949` n `67`; fx avg `0.0179` n `6`; index avg `0.0577` n `23`; metal avg `0.0912` n `18`; unknown avg `-0.0213` n `386`
- 1h: commodity avg `-0.0737` n `12`; crypto_alt avg `0.419` n `228`; crypto_major avg `0.1712` n `8`; equity avg `0.2184` n `67`; fx avg `0.0107` n `6`; index avg `0.1408` n `23`; metal avg `0.2517` n `18`; unknown avg `0.4832` n `386`
- 4h: commodity avg `-1.0928` n `12`; crypto_alt avg `0.4749` n `228`; crypto_major avg `0.4894` n `8`; equity avg `0.2954` n `67`; fx avg `-0.02` n `6`; index avg `0.1351` n `23`; metal avg `0.3483` n `18`; unknown avg `0.6532` n `386`
- 24h: commodity avg `-2.3164` n `12`; crypto_alt avg `2.8694` n `228`; crypto_major avg `1.2244` n `8`; equity avg `1.6907` n `67`; fx avg `0.111` n `6`; index avg `1.0629` n `23`; metal avg `0.9567` n `18`; unknown avg `1.6611` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0402`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0399`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0371`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0368`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0358`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0356`, n `668`, weak_sample_signal
