# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T21:37:26.116847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.2085` n `228`; crypto_major avg `-0.1688` n `8`; equity avg `-0.0265` n `78`; fx avg `-0.0098` n `6`; index avg `-0.0088` n `23`; metal avg `-0.0163` n `18`; unknown avg `0.0101` n `687`
- 1h: commodity avg `0.0456` n `12`; crypto_alt avg `0.1226` n `228`; crypto_major avg `0.0642` n `8`; equity avg `0.034` n `78`; fx avg `-0.0092` n `6`; index avg `-0.0111` n `23`; metal avg `0.0471` n `18`; unknown avg `-0.5008` n `687`
- 4h: commodity avg `0.1058` n `12`; crypto_alt avg `-0.4538` n `228`; crypto_major avg `-0.0798` n `8`; equity avg `-0.0317` n `78`; fx avg `-0.0572` n `6`; index avg `-0.0403` n `23`; metal avg `0.1461` n `18`; unknown avg `-0.2674` n `687`
- 24h: commodity avg `0.3469` n `12`; crypto_alt avg `-3.7823` n `228`; crypto_major avg `-4.6626` n `8`; equity avg `0.6988` n `78`; fx avg `-0.1528` n `6`; index avg `0.2089` n `23`; metal avg `-4.1165` n `18`; unknown avg `-0.576` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
