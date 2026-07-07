# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T22:52:31.199420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `0.0217` n `229`; crypto_major avg `-0.0118` n `8`; equity avg `-0.0104` n `91`; fx avg `0.0258` n `6`; index avg `-0.003` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.0699` n `763`
- 1h: commodity avg `0.0229` n `12`; crypto_alt avg `0.1491` n `229`; crypto_major avg `0.2517` n `8`; equity avg `0.0198` n `91`; fx avg `0.0112` n `6`; index avg `-0.023` n `25`; metal avg `-0.1255` n `20`; unknown avg `-0.0601` n `763`
- 4h: commodity avg `0.3782` n `12`; crypto_alt avg `-0.7781` n `229`; crypto_major avg `-0.4439` n `8`; equity avg `-0.2616` n `91`; fx avg `0.0039` n `6`; index avg `-0.0675` n `25`; metal avg `-0.3102` n `20`; unknown avg `-0.0533` n `761`
- 24h: commodity avg `0.9603` n `12`; crypto_alt avg `-2.7629` n `229`; crypto_major avg `-1.8161` n `8`; equity avg `-3.3438` n `91`; fx avg `-0.2723` n `6`; index avg `-0.601` n `25`; metal avg `-0.6908` n `20`; unknown avg `-0.159` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
