# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T17:42:33.907261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.1233` n `228`; crypto_major avg `-0.0327` n `8`; equity avg `-0.0567` n `86`; fx avg `-0.0049` n `6`; index avg `-0.0142` n `23`; metal avg `-0.0854` n `20`; unknown avg `-0.1711` n `764`
- 1h: commodity avg `0.037` n `12`; crypto_alt avg `-0.2764` n `228`; crypto_major avg `-0.103` n `8`; equity avg `-0.1128` n `86`; fx avg `0.0001` n `6`; index avg `-0.0331` n `23`; metal avg `-0.1042` n `20`; unknown avg `-0.5449` n `764`
- 4h: commodity avg `-0.0451` n `12`; crypto_alt avg `-0.4363` n `228`; crypto_major avg `-0.187` n `8`; equity avg `0.8505` n `86`; fx avg `-0.0579` n `6`; index avg `0.1066` n `23`; metal avg `0.0119` n `20`; unknown avg `-0.6638` n `764`
- 24h: commodity avg `-0.4799` n `12`; crypto_alt avg `-3.5528` n `228`; crypto_major avg `-3.7726` n `8`; equity avg `-2.8119` n `86`; fx avg `-0.1779` n `6`; index avg `-0.9041` n `23`; metal avg `-0.9081` n `20`; unknown avg `-0.182` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
