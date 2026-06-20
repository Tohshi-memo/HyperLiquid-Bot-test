# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T15:07:26.475208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0682` n `12`; crypto_alt avg `-0.0633` n `228`; crypto_major avg `-0.1235` n `8`; equity avg `-0.0275` n `78`; fx avg `0.0` n `6`; index avg `-0.008` n `23`; metal avg `-0.0201` n `18`; unknown avg `0.062` n `701`
- 1h: commodity avg `-0.1912` n `12`; crypto_alt avg `1.1968` n `228`; crypto_major avg `1.0788` n `8`; equity avg `0.3561` n `78`; fx avg `0.0288` n `6`; index avg `0.0173` n `23`; metal avg `0.0622` n `18`; unknown avg `0.8312` n `701`
- 4h: commodity avg `0.1281` n `12`; crypto_alt avg `-0.0653` n `228`; crypto_major avg `0.0131` n `8`; equity avg `0.0328` n `78`; fx avg `0.0197` n `6`; index avg `-0.0142` n `23`; metal avg `0.0199` n `18`; unknown avg `1.0023` n `573`
- 24h: commodity avg `0.6015` n `12`; crypto_alt avg `-3.1014` n `228`; crypto_major avg `-3.3867` n `8`; equity avg `1.1437` n `78`; fx avg `-0.0564` n `6`; index avg `0.2795` n `23`; metal avg `-4.0874` n `18`; unknown avg `-0.3058` n `492`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
