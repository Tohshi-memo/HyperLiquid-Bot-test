# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T16:07:47.931356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.055` n `12`; crypto_alt avg `0.0638` n `230`; crypto_major avg `0.0679` n `8`; equity avg `0.3614` n `100`; fx avg `-0.0079` n `6`; index avg `0.0438` n `25`; metal avg `0.0199` n `20`; unknown avg `-0.0016` n `773`
- 1h: commodity avg `-0.3104` n `12`; crypto_alt avg `0.3841` n `230`; crypto_major avg `0.3621` n `8`; equity avg `0.89` n `100`; fx avg `0.0178` n `6`; index avg `0.1791` n `25`; metal avg `0.1784` n `20`; unknown avg `-0.0208` n `773`
- 4h: commodity avg `-0.2329` n `12`; crypto_alt avg `-0.7428` n `230`; crypto_major avg `-0.6535` n `8`; equity avg `-1.3756` n `100`; fx avg `0.0277` n `6`; index avg `-0.0411` n `25`; metal avg `0.0971` n `20`; unknown avg `13.1543` n `773`
- 24h: commodity avg `-0.5746` n `12`; crypto_alt avg `-1.409` n `230`; crypto_major avg `-1.123` n `8`; equity avg `-1.6951` n `100`; fx avg `-0.1149` n `6`; index avg `-0.1434` n `25`; metal avg `0.1808` n `20`; unknown avg `13.6107` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1129`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.111`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.103`, n `666`, weak_sample_signal
