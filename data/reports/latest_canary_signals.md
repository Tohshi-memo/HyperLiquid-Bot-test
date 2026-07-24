# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T21:22:24.530942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0131` n `12`; crypto_alt avg `-0.0199` n `230`; crypto_major avg `-0.1667` n `8`; equity avg `-0.0702` n `100`; fx avg `-0.0014` n `6`; index avg `0.0007` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.0758` n `774`
- 1h: commodity avg `0.1354` n `12`; crypto_alt avg `-0.2913` n `230`; crypto_major avg `-0.4093` n `8`; equity avg `-0.1566` n `100`; fx avg `-0.0143` n `6`; index avg `-0.0123` n `25`; metal avg `0.0108` n `20`; unknown avg `-0.0357` n `774`
- 4h: commodity avg `0.3327` n `12`; crypto_alt avg `-0.3241` n `230`; crypto_major avg `-0.2876` n `8`; equity avg `-0.9291` n `100`; fx avg `-0.0178` n `6`; index avg `-0.1508` n `25`; metal avg `-0.1164` n `20`; unknown avg `-0.1111` n `773`
- 24h: commodity avg `-0.2647` n `12`; crypto_alt avg `-1.1913` n `230`; crypto_major avg `-1.2449` n `8`; equity avg `-3.4309` n `100`; fx avg `-0.1736` n `6`; index avg `-0.4872` n `25`; metal avg `-0.0402` n `20`; unknown avg `13.9258` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1269`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1228`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1134`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.11`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
