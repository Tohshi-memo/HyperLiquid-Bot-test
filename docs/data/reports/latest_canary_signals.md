# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T21:52:25.671315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `-0.0819` n `228`; crypto_major avg `-0.1159` n `8`; equity avg `-0.045` n `78`; fx avg `-0.0245` n `6`; index avg `0.0061` n `23`; metal avg `-0.0026` n `18`; unknown avg `0.2561` n `687`
- 1h: commodity avg `0.0366` n `12`; crypto_alt avg `-0.2373` n `228`; crypto_major avg `-0.2859` n `8`; equity avg `-0.0553` n `78`; fx avg `-0.0831` n `6`; index avg `0.0017` n `23`; metal avg `-0.0102` n `18`; unknown avg `-0.389` n `687`
- 4h: commodity avg `0.1084` n `12`; crypto_alt avg `-0.6489` n `228`; crypto_major avg `-0.3256` n `8`; equity avg `-0.075` n `78`; fx avg `-0.1096` n `6`; index avg `0.0002` n `23`; metal avg `0.1409` n `18`; unknown avg `-0.322` n `687`
- 24h: commodity avg `0.36` n `12`; crypto_alt avg `-3.8609` n `228`; crypto_major avg `-4.7731` n `8`; equity avg `0.6554` n `78`; fx avg `-0.177` n `6`; index avg `0.2152` n `23`; metal avg `-4.1195` n `18`; unknown avg `-0.5797` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
