# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T16:22:24.947964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0499` n `12`; crypto_alt avg `0.0916` n `228`; crypto_major avg `0.2424` n `8`; equity avg `0.2062` n `74`; fx avg `-0.0018` n `6`; index avg `0.0473` n `23`; metal avg `0.0463` n `18`; unknown avg `4.8865` n `516`
- 1h: commodity avg `0.1077` n `12`; crypto_alt avg `0.0582` n `228`; crypto_major avg `0.2584` n `8`; equity avg `0.1855` n `74`; fx avg `-0.0058` n `6`; index avg `0.1001` n `23`; metal avg `0.0432` n `18`; unknown avg `-0.0304` n `516`
- 4h: commodity avg `0.3082` n `12`; crypto_alt avg `1.0101` n `228`; crypto_major avg `1.0367` n `8`; equity avg `0.5974` n `74`; fx avg `-0.0007` n `6`; index avg `0.1279` n `23`; metal avg `0.0063` n `18`; unknown avg `0.37` n `516`
- 24h: commodity avg `0.3771` n `12`; crypto_alt avg `2.7477` n `228`; crypto_major avg `3.0999` n `8`; equity avg `1.9783` n `74`; fx avg `-0.0258` n `6`; index avg `0.3302` n `23`; metal avg `0.6078` n `18`; unknown avg `-4.3337` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
