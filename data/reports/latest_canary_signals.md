# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T08:52:30.120922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `-0.0325` n `233`; crypto_major avg `-0.0337` n `8`; equity avg `-0.0687` n `134`; fx avg `-0.0032` n `6`; index avg `-0.0178` n `26`; metal avg `-0.0386` n `20`; unknown avg `0.3115` n `797`
- 1h: commodity avg `0.0861` n `12`; crypto_alt avg `0.0128` n `233`; crypto_major avg `-0.0109` n `8`; equity avg `-0.1898` n `134`; fx avg `0.0282` n `6`; index avg `-0.0315` n `26`; metal avg `-0.1228` n `20`; unknown avg `1.1101` n `789`
- 4h: commodity avg `0.105` n `12`; crypto_alt avg `-0.4027` n `233`; crypto_major avg `-0.4274` n `8`; equity avg `-0.2911` n `134`; fx avg `0.076` n `6`; index avg `-0.0327` n `26`; metal avg `-0.1769` n `20`; unknown avg `0.1697` n `765`
- 24h: commodity avg `0.0295` n `12`; crypto_alt avg `-4.8058` n `233`; crypto_major avg `-3.3066` n `8`; equity avg `-1.5052` n `134`; fx avg `0.0737` n `6`; index avg `-0.1606` n `26`; metal avg `0.0533` n `20`; unknown avg `0.5298` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
