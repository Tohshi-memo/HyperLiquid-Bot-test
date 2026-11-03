# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T04:07:27.004936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `0.0318` n `239`; crypto_major avg `-0.0155` n `8`; equity avg `-0.1779` n `157`; fx avg `0.0034` n `6`; index avg `-0.0225` n `27`; metal avg `0.0013` n `20`; unknown avg `0.2626` n `1244`
- 1h: commodity avg `0.0552` n `13`; crypto_alt avg `0.129` n `239`; crypto_major avg `0.0848` n `8`; equity avg `-0.3479` n `157`; fx avg `0.0288` n `6`; index avg `-0.0469` n `27`; metal avg `-0.126` n `20`; unknown avg `-0.4647` n `1244`
- 4h: commodity avg `0.1646` n `13`; crypto_alt avg `-0.6555` n `239`; crypto_major avg `-0.1626` n `8`; equity avg `-0.3196` n `157`; fx avg `-0.054` n `6`; index avg `-0.0355` n `27`; metal avg `-0.3237` n `20`; unknown avg `0.2969` n `1244`
- 24h: commodity avg `-0.8601` n `13`; crypto_alt avg `-3.6016` n `238`; crypto_major avg `-2.5476` n `8`; equity avg `-4.4167` n `157`; fx avg `-0.0175` n `6`; index avg `-0.3293` n `27`; metal avg `-0.1568` n `20`; unknown avg `12.5681` n `1010`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
