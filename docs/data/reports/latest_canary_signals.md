# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T16:22:31.408301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `0.0261` n `230`; crypto_major avg `0.0514` n `8`; equity avg `-0.0259` n `98`; fx avg `0.0085` n `6`; index avg `0.0021` n `25`; metal avg `-0.0324` n `20`; unknown avg `-0.0432` n `770`
- 1h: commodity avg `-0.0604` n `12`; crypto_alt avg `0.4889` n `230`; crypto_major avg `0.7429` n `8`; equity avg `0.5252` n `98`; fx avg `0.007` n `6`; index avg `0.1119` n `25`; metal avg `0.06` n `20`; unknown avg `-0.0164` n `770`
- 4h: commodity avg `-0.1663` n `12`; crypto_alt avg `0.6412` n `230`; crypto_major avg `0.9769` n `8`; equity avg `0.1712` n `98`; fx avg `-0.0724` n `6`; index avg `0.0616` n `25`; metal avg `0.1457` n `20`; unknown avg `0.0021` n `770`
- 24h: commodity avg `-0.6423` n `12`; crypto_alt avg `1.3283` n `230`; crypto_major avg `1.2655` n `8`; equity avg `1.0122` n `97`; fx avg `-0.139` n `6`; index avg `0.3064` n `25`; metal avg `0.2901` n `20`; unknown avg `0.0958` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0952`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0847`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0816`, n `666`, weak_sample_signal
