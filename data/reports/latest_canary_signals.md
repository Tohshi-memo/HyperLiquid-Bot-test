# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T09:22:30.199867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `13`; crypto_alt avg `-0.2136` n `238`; crypto_major avg `-0.1711` n `8`; equity avg `0.0341` n `156`; fx avg `0.0152` n `6`; index avg `0.0093` n `27`; metal avg `-0.012` n `20`; unknown avg `0.5862` n `1262`
- 1h: commodity avg `-0.1099` n `13`; crypto_alt avg `0.0503` n `238`; crypto_major avg `0.1965` n `8`; equity avg `0.214` n `156`; fx avg `0.0497` n `6`; index avg `0.0475` n `27`; metal avg `-0.007` n `20`; unknown avg `0.9565` n `1258`
- 4h: commodity avg `-0.129` n `13`; crypto_alt avg `-0.9021` n `238`; crypto_major avg `-0.3128` n `8`; equity avg `0.0074` n `156`; fx avg `0.1066` n `6`; index avg `-0.0603` n `27`; metal avg `-0.0242` n `20`; unknown avg `1.5663` n `1151`
- 24h: commodity avg `-0.5959` n `13`; crypto_alt avg `-1.8058` n `238`; crypto_major avg `-0.26` n `8`; equity avg `0.9587` n `156`; fx avg `0.3029` n `6`; index avg `0.3058` n `27`; metal avg `0.0802` n `20`; unknown avg `2.4963` n `1065`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.172`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
