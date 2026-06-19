# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T21:22:31.337996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0475` n `12`; crypto_alt avg `0.0442` n `228`; crypto_major avg `-0.0088` n `8`; equity avg `0.0213` n `78`; fx avg `-0.0104` n `6`; index avg `0.0118` n `23`; metal avg `0.0` n `18`; unknown avg `55.0726` n `687`
- 1h: commodity avg `0.0786` n `12`; crypto_alt avg `0.3542` n `228`; crypto_major avg `0.3485` n `8`; equity avg `0.0593` n `78`; fx avg `-0.0406` n `6`; index avg `-0.0063` n `23`; metal avg `0.0649` n `18`; unknown avg `-0.4844` n `687`
- 4h: commodity avg `0.0851` n `12`; crypto_alt avg `0.0281` n `228`; crypto_major avg `0.374` n `8`; equity avg `0.0325` n `78`; fx avg `-0.0487` n `6`; index avg `-0.0107` n `23`; metal avg `0.1665` n `18`; unknown avg `-0.258` n `687`
- 24h: commodity avg `0.3475` n `12`; crypto_alt avg `-3.587` n `228`; crypto_major avg `-4.502` n `8`; equity avg `0.725` n `78`; fx avg `-0.143` n `6`; index avg `0.2176` n `23`; metal avg `-4.1012` n `18`; unknown avg `-0.593` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
