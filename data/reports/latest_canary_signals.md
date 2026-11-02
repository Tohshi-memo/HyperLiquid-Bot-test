# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T20:52:26.749413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0393` n `13`; crypto_alt avg `0.1173` n `239`; crypto_major avg `0.0593` n `8`; equity avg `0.0353` n `157`; fx avg `0.0073` n `6`; index avg `0.0016` n `27`; metal avg `-0.013` n `20`; unknown avg `1.0143` n `1264`
- 1h: commodity avg `-0.1437` n `13`; crypto_alt avg `0.3404` n `239`; crypto_major avg `0.117` n `8`; equity avg `-0.3769` n `157`; fx avg `0.0097` n `6`; index avg `-0.0725` n `27`; metal avg `-0.0125` n `20`; unknown avg `15.2735` n `1236`
- 4h: commodity avg `-0.2645` n `13`; crypto_alt avg `-1.3933` n `239`; crypto_major avg `-1.1223` n `8`; equity avg `-2.5098` n `157`; fx avg `-0.0009` n `6`; index avg `-0.3035` n `27`; metal avg `-0.2551` n `20`; unknown avg `29.8893` n `1170`
- 24h: commodity avg `-1.439` n `13`; crypto_alt avg `-2.9366` n `238`; crypto_major avg `-1.6075` n `8`; equity avg `-3.1793` n `157`; fx avg `0.2764` n `6`; index avg `-0.0528` n `27`; metal avg `0.1723` n `20`; unknown avg `9.4553` n `1016`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
