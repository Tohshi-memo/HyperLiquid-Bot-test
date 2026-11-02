# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T21:07:30.046143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0402` n `13`; crypto_alt avg `0.0802` n `239`; crypto_major avg `0.1164` n `8`; equity avg `0.1974` n `157`; fx avg `-0.0019` n `6`; index avg `0.0354` n `27`; metal avg `0.0162` n `20`; unknown avg `0.5225` n `1250`
- 1h: commodity avg `-0.0405` n `13`; crypto_alt avg `-0.0003` n `239`; crypto_major avg `-0.0495` n `8`; equity avg `-0.5601` n `157`; fx avg `0.0033` n `6`; index avg `-0.0853` n `27`; metal avg `-0.0433` n `20`; unknown avg `31.2979` n `1250`
- 4h: commodity avg `-0.183` n `13`; crypto_alt avg `-1.2516` n `239`; crypto_major avg `-0.9123` n `8`; equity avg `-2.352` n `157`; fx avg `-0.0133` n `6`; index avg `-0.2729` n `27`; metal avg `-0.2385` n `20`; unknown avg `9.867` n `1160`
- 24h: commodity avg `-1.4039` n `13`; crypto_alt avg `-2.8726` n `238`; crypto_major avg `-1.5196` n `8`; equity avg `-3.0212` n `157`; fx avg `0.2768` n `6`; index avg `-0.0062` n `27`; metal avg `0.192` n `20`; unknown avg `9.5921` n `1014`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
