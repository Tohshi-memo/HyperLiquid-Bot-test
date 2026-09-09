# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T20:22:33.365542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `0.0319` n `233`; crypto_major avg `-0.0127` n `8`; equity avg `0.0373` n `134`; fx avg `-0.0005` n `6`; index avg `0.006` n `26`; metal avg `-0.0142` n `20`; unknown avg `3.1251` n `795`
- 1h: commodity avg `0.0766` n `12`; crypto_alt avg `-1.0327` n `233`; crypto_major avg `-0.9155` n `8`; equity avg `-0.2485` n `134`; fx avg `0.0055` n `6`; index avg `-0.0317` n `26`; metal avg `-0.1037` n `20`; unknown avg `41.8269` n `767`
- 4h: commodity avg `-0.006` n `12`; crypto_alt avg `-0.6222` n `233`; crypto_major avg `-0.6396` n `8`; equity avg `-0.0527` n `134`; fx avg `0.0173` n `6`; index avg `0.0403` n `26`; metal avg `-0.0369` n `20`; unknown avg `1.6432` n `761`
- 24h: commodity avg `0.149` n `12`; crypto_alt avg `-1.658` n `233`; crypto_major avg `-1.046` n `8`; equity avg `-0.3674` n `134`; fx avg `-0.0326` n `6`; index avg `-0.1404` n `26`; metal avg `0.4522` n `20`; unknown avg `7.5962` n `695`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
