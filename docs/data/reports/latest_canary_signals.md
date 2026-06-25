# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T03:07:29.819217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0952` n `12`; crypto_alt avg `-0.0001` n `228`; crypto_major avg `0.0995` n `8`; equity avg `0.1124` n `86`; fx avg `-0.0085` n `6`; index avg `0.0271` n `23`; metal avg `-0.017` n `20`; unknown avg `-0.5457` n `764`
- 1h: commodity avg `-0.0204` n `12`; crypto_alt avg `-0.1345` n `228`; crypto_major avg `-0.1224` n `8`; equity avg `-0.0607` n `86`; fx avg `-0.0228` n `6`; index avg `0.0165` n `23`; metal avg `0.0603` n `20`; unknown avg `-0.029` n `748`
- 4h: commodity avg `-0.1318` n `12`; crypto_alt avg `-0.033` n `228`; crypto_major avg `0.0362` n `8`; equity avg `-0.4429` n `86`; fx avg `0.0838` n `6`; index avg `-0.0739` n `23`; metal avg `-0.2467` n `20`; unknown avg `0.1343` n `748`
- 24h: commodity avg `-0.4839` n `12`; crypto_alt avg `-1.9502` n `228`; crypto_major avg `-1.5568` n `8`; equity avg `0.4174` n `86`; fx avg `0.0718` n `6`; index avg `0.7822` n `23`; metal avg `-1.5445` n `20`; unknown avg `-0.4062` n `700`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
