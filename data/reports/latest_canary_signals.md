# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T03:37:28.354001+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `0.0301` n `228`; crypto_major avg `0.0539` n `8`; equity avg `0.0325` n `78`; fx avg `0.0` n `6`; index avg `0.0012` n `23`; metal avg `0.0001` n `18`; unknown avg `0.3994` n `687`
- 1h: commodity avg `0.0572` n `12`; crypto_alt avg `0.0533` n `228`; crypto_major avg `0.1133` n `8`; equity avg `0.0365` n `78`; fx avg `0.0113` n `6`; index avg `0.003` n `23`; metal avg `-0.0321` n `18`; unknown avg `0.015` n `687`
- 4h: commodity avg `0.1447` n `12`; crypto_alt avg `-0.2754` n `228`; crypto_major avg `-0.0637` n `8`; equity avg `0.0466` n `78`; fx avg `0.0383` n `6`; index avg `0.0367` n `23`; metal avg `-0.0749` n `18`; unknown avg `-0.6247` n `671`
- 24h: commodity avg `0.4569` n `12`; crypto_alt avg `-3.727` n `228`; crypto_major avg `-4.4672` n `8`; equity avg `0.985` n `78`; fx avg `-0.0758` n `6`; index avg `0.2977` n `23`; metal avg `-4.1639` n `18`; unknown avg `-0.5933` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
