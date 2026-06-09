# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T20:52:22.311019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8934` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.2228` n `12`; crypto_alt avg `-0.1015` n `228`; crypto_major avg `-0.0` n `8`; equity avg `0.0347` n `74`; fx avg `-0.0023` n `6`; index avg `0.0019` n `23`; metal avg `0.0195` n `18`; unknown avg `-0.0337` n `547`
- 1h: commodity avg `0.1921` n `12`; crypto_alt avg `0.3206` n `228`; crypto_major avg `0.2712` n `8`; equity avg `0.5302` n `74`; fx avg `-0.0266` n `6`; index avg `0.5834` n `23`; metal avg `0.116` n `18`; unknown avg `0.2879` n `547`
- 4h: commodity avg `0.2391` n `12`; crypto_alt avg `2.1891` n `228`; crypto_major avg `1.403` n `8`; equity avg `3.2964` n `74`; fx avg `-0.0728` n `6`; index avg `2.1376` n `23`; metal avg `0.5915` n `18`; unknown avg `0.7086` n `547`
- 24h: commodity avg `-0.732` n `12`; crypto_alt avg `-1.5881` n `228`; crypto_major avg `-2.3962` n `8`; equity avg `-1.6476` n `74`; fx avg `0.061` n `6`; index avg `-0.7817` n `23`; metal avg `-1.4134` n `18`; unknown avg `-1.0207` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0416`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0409`, n `668`, weak_sample_signal
