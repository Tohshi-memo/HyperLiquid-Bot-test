# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T15:19:19.984392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `12`; crypto_alt avg `0.5621` n `228`; crypto_major avg `0.5634` n `8`; equity avg `0.1281` n `78`; fx avg `0.0` n `6`; index avg `0.006` n `23`; metal avg `0.0261` n `18`; unknown avg `0.1615` n `701`
- 1h: commodity avg `-0.1365` n `12`; crypto_alt avg `1.6418` n `228`; crypto_major avg `1.5709` n `8`; equity avg `0.4232` n `78`; fx avg `0.0015` n `6`; index avg `0.0195` n `23`; metal avg `0.1069` n `18`; unknown avg `1.7446` n `701`
- 4h: commodity avg `0.1682` n `12`; crypto_alt avg `0.5831` n `228`; crypto_major avg `0.5877` n `8`; equity avg `0.1271` n `78`; fx avg `0.0157` n `6`; index avg `-0.0077` n `23`; metal avg `0.041` n `18`; unknown avg `1.6967` n `573`
- 24h: commodity avg `0.6181` n `12`; crypto_alt avg `-2.5609` n `228`; crypto_major avg `-2.8452` n `8`; equity avg `1.279` n `78`; fx avg `-0.0564` n `6`; index avg `0.2854` n `23`; metal avg `-4.0631` n `18`; unknown avg `-0.0474` n `492`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
