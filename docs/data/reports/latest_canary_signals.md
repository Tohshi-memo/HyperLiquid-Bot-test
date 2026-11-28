# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T06:37:24.898161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `0.2162` n `239`; crypto_major avg `0.1539` n `8`; equity avg `0.1451` n `168`; fx avg `0.0046` n `6`; index avg `0.0024` n `27`; metal avg `0.0277` n `20`; unknown avg `48.0876` n `1265`
- 1h: commodity avg `-0.0137` n `13`; crypto_alt avg `0.059` n `239`; crypto_major avg `0.1568` n `8`; equity avg `0.0391` n `168`; fx avg `0.0133` n `6`; index avg `-0.0071` n `27`; metal avg `0.0085` n `20`; unknown avg `0.3767` n `1229`
- 4h: commodity avg `-0.0146` n `13`; crypto_alt avg `-1.4123` n `239`; crypto_major avg `-0.523` n `8`; equity avg `-0.1956` n `168`; fx avg `0.0186` n `6`; index avg `-0.0403` n `27`; metal avg `-0.0562` n `20`; unknown avg `0.5136` n `1213`
- 24h: commodity avg `-0.8469` n `13`; crypto_alt avg `-2.9991` n `239`; crypto_major avg `-2.446` n `8`; equity avg `-0.5106` n `168`; fx avg `-0.1233` n `6`; index avg `-0.0073` n `27`; metal avg `-0.236` n `20`; unknown avg `215.4217` n `967`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
