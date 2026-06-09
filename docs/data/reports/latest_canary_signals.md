# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T05:37:26.215569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0969` n `12`; crypto_alt avg `0.2566` n `228`; crypto_major avg `0.3084` n `8`; equity avg `0.198` n `74`; fx avg `-0.0268` n `6`; index avg `0.1268` n `23`; metal avg `0.2815` n `18`; unknown avg `-0.0178` n `517`
- 1h: commodity avg `-0.0924` n `12`; crypto_alt avg `0.538` n `228`; crypto_major avg `0.3522` n `8`; equity avg `0.1109` n `74`; fx avg `-0.0482` n `6`; index avg `0.0788` n `23`; metal avg `0.3798` n `18`; unknown avg `153.8591` n `517`
- 4h: commodity avg `-0.2099` n `12`; crypto_alt avg `1.0223` n `228`; crypto_major avg `1.0643` n `8`; equity avg `1.1348` n `74`; fx avg `-0.0498` n `6`; index avg `0.5408` n `23`; metal avg `0.1982` n `18`; unknown avg `-0.3352` n `517`
- 24h: commodity avg `-1.6621` n `12`; crypto_alt avg `1.6995` n `228`; crypto_major avg `2.2761` n `8`; equity avg `3.1991` n `74`; fx avg `-0.239` n `6`; index avg `1.4651` n `23`; metal avg `1.5594` n `18`; unknown avg `-2.7929` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
