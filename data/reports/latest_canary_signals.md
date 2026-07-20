# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T08:52:26.362909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `0.2574` n `230`; crypto_major avg `0.1902` n `8`; equity avg `0.0768` n `98`; fx avg `0.0021` n `6`; index avg `0.0093` n `25`; metal avg `-0.0651` n `20`; unknown avg `-0.0093` n `770`
- 1h: commodity avg `-0.2048` n `12`; crypto_alt avg `-0.128` n `230`; crypto_major avg `-0.1211` n `8`; equity avg `-0.0025` n `98`; fx avg `-0.0013` n `6`; index avg `0.0088` n `25`; metal avg `-0.0391` n `20`; unknown avg `0.0038` n `769`
- 4h: commodity avg `-0.4964` n `12`; crypto_alt avg `-0.0179` n `230`; crypto_major avg `-0.4433` n `8`; equity avg `-0.3202` n `98`; fx avg `0.02` n `6`; index avg `-0.0796` n `25`; metal avg `0.0436` n `20`; unknown avg `-0.0794` n `747`
- 24h: commodity avg `-0.5828` n `12`; crypto_alt avg `-0.24` n `230`; crypto_major avg `-0.7356` n `8`; equity avg `-0.0524` n `97`; fx avg `-0.0178` n `6`; index avg `0.0198` n `25`; metal avg `0.1697` n `20`; unknown avg `-0.0551` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.09`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0811`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0766`, n `666`, weak_sample_signal
