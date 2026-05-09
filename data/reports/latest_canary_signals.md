# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T07:22:20.563634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.026` n `12`; crypto_alt avg `0.0495` n `228`; crypto_major avg `0.0688` n `8`; equity avg `-0.0142` n `65`; fx avg `0.0011` n `5`; index avg `0.015` n `23`; metal avg `0.0053` n `18`; unknown avg `-0.1143` n `376`
- 1h: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.3493` n `228`; crypto_major avg `-0.0733` n `8`; equity avg `0.0095` n `65`; fx avg `0.0011` n `5`; index avg `0.0351` n `23`; metal avg `0.0021` n `18`; unknown avg `0.1456` n `376`
- 4h: commodity avg `0.0963` n `12`; crypto_alt avg `-0.4455` n `228`; crypto_major avg `-0.2359` n `8`; equity avg `-0.0542` n `65`; fx avg `0.02` n `5`; index avg `0.0742` n `23`; metal avg `-0.0641` n `18`; unknown avg `-0.3964` n `355`
- 24h: commodity avg `-0.0768` n `12`; crypto_alt avg `4.5165` n `228`; crypto_major avg `2.9456` n `8`; equity avg `3.3781` n `65`; fx avg `-0.0008` n `5`; index avg `1.3202` n `23`; metal avg `0.1611` n `18`; unknown avg `1.1929` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
