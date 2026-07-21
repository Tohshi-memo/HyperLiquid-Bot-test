# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T00:52:29.597522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `0.0718` n `230`; crypto_major avg `0.0595` n `8`; equity avg `0.128` n `98`; fx avg `0.0122` n `6`; index avg `0.0475` n `25`; metal avg `0.0571` n `20`; unknown avg `0.1454` n `771`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `0.406` n `230`; crypto_major avg `0.385` n `8`; equity avg `0.3594` n `98`; fx avg `0.0246` n `6`; index avg `0.125` n `25`; metal avg `0.141` n `20`; unknown avg `0.1622` n `770`
- 4h: commodity avg `0.0511` n `12`; crypto_alt avg `0.2825` n `230`; crypto_major avg `0.2787` n `8`; equity avg `0.4626` n `98`; fx avg `0.0281` n `6`; index avg `0.0581` n `25`; metal avg `0.1192` n `20`; unknown avg `-0.3929` n `770`
- 24h: commodity avg `-0.2759` n `12`; crypto_alt avg `1.6837` n `230`; crypto_major avg `1.424` n `8`; equity avg `-0.1925` n `98`; fx avg `-0.1314` n `6`; index avg `-0.0285` n `25`; metal avg `0.1574` n `20`; unknown avg `-0.0407` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1077`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1015`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0925`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0811`, n `666`, weak_sample_signal
