# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T02:07:24.295234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `-0.3797` n `228`; crypto_major avg `-0.4092` n `8`; equity avg `-0.1195` n `74`; fx avg `-0.0096` n `6`; index avg `-0.0176` n `23`; metal avg `-0.0162` n `18`; unknown avg `1.0367` n `425`
- 1h: commodity avg `-0.0892` n `12`; crypto_alt avg `-1.2691` n `228`; crypto_major avg `-1.1053` n `8`; equity avg `-1.0344` n `74`; fx avg `-0.0232` n `6`; index avg `-0.5229` n `23`; metal avg `-0.1417` n `18`; unknown avg `0.7957` n `425`
- 4h: commodity avg `0.7895` n `12`; crypto_alt avg `-0.8914` n `228`; crypto_major avg `-0.4466` n `8`; equity avg `-1.4853` n `74`; fx avg `-0.039` n `6`; index avg `-0.4808` n `23`; metal avg `-0.2796` n `18`; unknown avg `0.7352` n `425`
- 24h: commodity avg `-1.202` n `12`; crypto_alt avg `-6.5775` n `228`; crypto_major avg `-5.7519` n `8`; equity avg `-6.5373` n `74`; fx avg `-0.2346` n `6`; index avg `-3.9787` n `23`; metal avg `-3.7578` n `18`; unknown avg `-0.3438` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
