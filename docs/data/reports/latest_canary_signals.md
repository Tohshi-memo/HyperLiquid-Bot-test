# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T01:52:26.879138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0498` n `12`; crypto_alt avg `-0.1707` n `228`; crypto_major avg `-0.1856` n `8`; equity avg `-0.1066` n `86`; fx avg `-0.0039` n `6`; index avg `0.0166` n `23`; metal avg `-0.1075` n `20`; unknown avg `0.0311` n `764`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `-0.0986` n `228`; crypto_major avg `0.1483` n `8`; equity avg `-0.1727` n `86`; fx avg `-0.0119` n `6`; index avg `0.0013` n `23`; metal avg `-0.0707` n `20`; unknown avg `-0.4268` n `764`
- 4h: commodity avg `-0.0697` n `12`; crypto_alt avg `0.2143` n `228`; crypto_major avg `0.7104` n `8`; equity avg `0.3872` n `86`; fx avg `0.0185` n `6`; index avg `0.1165` n `23`; metal avg `-0.2118` n `20`; unknown avg `-0.1048` n `756`
- 24h: commodity avg `-0.4585` n `12`; crypto_alt avg `-1.5039` n `228`; crypto_major avg `-1.9931` n `8`; equity avg `-1.3607` n `86`; fx avg `-0.1472` n `6`; index avg `-0.4424` n `23`; metal avg `-0.8955` n `20`; unknown avg `0.544` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
