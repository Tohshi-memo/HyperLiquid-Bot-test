# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T22:22:34.646466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `0.386` n `228`; crypto_major avg `0.3938` n `8`; equity avg `0.0341` n `78`; fx avg `0.0312` n `6`; index avg `-0.0044` n `23`; metal avg `0.002` n `18`; unknown avg `-0.157` n `687`
- 1h: commodity avg `0.1435` n `12`; crypto_alt avg `-0.0337` n `228`; crypto_major avg `-0.0013` n `8`; equity avg `-0.0445` n `78`; fx avg `0.0382` n `6`; index avg `-0.0117` n `23`; metal avg `-0.0106` n `18`; unknown avg `0.0014` n `687`
- 4h: commodity avg `0.236` n `12`; crypto_alt avg `-0.2701` n `228`; crypto_major avg `-0.0799` n `8`; equity avg `-0.0404` n `78`; fx avg `-0.0136` n `6`; index avg `-0.0229` n `23`; metal avg `0.1708` n `18`; unknown avg `-0.506` n `687`
- 24h: commodity avg `0.4937` n `12`; crypto_alt avg `-3.619` n `228`; crypto_major avg `-4.5048` n `8`; equity avg `0.6806` n `78`; fx avg `-0.105` n `6`; index avg `0.2057` n `23`; metal avg `-4.1115` n `18`; unknown avg `-0.6666` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
