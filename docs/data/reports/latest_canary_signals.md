# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T06:22:24.036252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.1991` n `230`; crypto_major avg `0.1665` n `8`; equity avg `0.1226` n `100`; fx avg `0.0215` n `6`; index avg `0.0323` n `25`; metal avg `0.0974` n `20`; unknown avg `0.011` n `772`
- 1h: commodity avg `-0.128` n `12`; crypto_alt avg `0.2112` n `230`; crypto_major avg `0.2205` n `8`; equity avg `-0.1856` n `100`; fx avg `0.0358` n `6`; index avg `-0.0548` n `25`; metal avg `0.0278` n `20`; unknown avg `-0.0359` n `756`
- 4h: commodity avg `-0.141` n `12`; crypto_alt avg `0.4407` n `230`; crypto_major avg `0.3934` n `8`; equity avg `-0.1906` n `100`; fx avg `0.0315` n `6`; index avg `-0.0619` n `25`; metal avg `-0.0475` n `20`; unknown avg `0.1872` n `756`
- 24h: commodity avg `0.3375` n `12`; crypto_alt avg `-0.8381` n `230`; crypto_major avg `-1.3829` n `8`; equity avg `-1.9504` n `99`; fx avg `-0.0863` n `6`; index avg `-0.556` n `25`; metal avg `-0.9048` n `20`; unknown avg `-0.0018` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1065`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0919`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0876`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0872`, n `666`, weak_sample_signal
