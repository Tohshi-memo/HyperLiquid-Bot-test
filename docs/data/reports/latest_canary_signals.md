# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T22:25:13.006111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0552` n `12`; crypto_alt avg `0.0487` n `230`; crypto_major avg `0.0566` n `8`; equity avg `0.0936` n `100`; fx avg `-0.0034` n `6`; index avg `0.0186` n `25`; metal avg `-0.0163` n `20`; unknown avg `0.1494` n `775`
- 1h: commodity avg `-0.4418` n `12`; crypto_alt avg `0.7116` n `230`; crypto_major avg `0.6262` n `8`; equity avg `0.3924` n `100`; fx avg `0.0008` n `6`; index avg `0.1207` n `25`; metal avg `0.1623` n `20`; unknown avg `0.0663` n `775`
- 4h: commodity avg `-0.3194` n `12`; crypto_alt avg `0.6486` n `230`; crypto_major avg `0.6232` n `8`; equity avg `0.4119` n `100`; fx avg `0.0219` n `6`; index avg `0.0801` n `25`; metal avg `0.1966` n `20`; unknown avg `-0.2604` n `775`
- 24h: commodity avg `-0.7103` n `12`; crypto_alt avg `1.4203` n `230`; crypto_major avg `1.5642` n `8`; equity avg `1.021` n `100`; fx avg `0.0498` n `6`; index avg `0.2122` n `25`; metal avg `0.3802` n `20`; unknown avg `0.085` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
