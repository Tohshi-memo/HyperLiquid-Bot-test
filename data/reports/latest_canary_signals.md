# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T14:37:30.242437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1113` n `12`; crypto_alt avg `0.3638` n `230`; crypto_major avg `0.3394` n `8`; equity avg `0.3176` n `98`; fx avg `-0.0141` n `6`; index avg `0.048` n `25`; metal avg `0.1293` n `20`; unknown avg `0.4711` n `770`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.3772` n `230`; crypto_major avg `-0.5525` n `8`; equity avg `-0.9172` n `98`; fx avg `-0.0195` n `6`; index avg `-0.1317` n `25`; metal avg `0.0337` n `20`; unknown avg `0.1065` n `770`
- 4h: commodity avg `-0.0726` n `12`; crypto_alt avg `0.0584` n `230`; crypto_major avg `-0.0479` n `8`; equity avg `-0.381` n `98`; fx avg `-0.0697` n `6`; index avg `0.0391` n `25`; metal avg `-0.0174` n `20`; unknown avg `0.2852` n `770`
- 24h: commodity avg `-0.6062` n `12`; crypto_alt avg `0.4194` n `230`; crypto_major avg `-0.2924` n `8`; equity avg `0.2016` n `97`; fx avg `-0.0899` n `6`; index avg `0.1525` n `25`; metal avg `0.1847` n `20`; unknown avg `-0.0335` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0999`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0889`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0797`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
