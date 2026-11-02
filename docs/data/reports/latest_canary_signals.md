# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T09:57:50.095071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `13`; crypto_alt avg `0.0649` n `238`; crypto_major avg `0.0515` n `8`; equity avg `0.0971` n `156`; fx avg `-0.0031` n `6`; index avg `-0.005` n `27`; metal avg `-0.0309` n `20`; unknown avg `0.3593` n `1260`
- 1h: commodity avg `-0.0322` n `13`; crypto_alt avg `-0.2583` n `238`; crypto_major avg `-0.2962` n `8`; equity avg `0.11` n `156`; fx avg `0.0036` n `6`; index avg `0.0115` n `27`; metal avg `-0.1296` n `20`; unknown avg `2.0035` n `1256`
- 4h: commodity avg `-0.1749` n `13`; crypto_alt avg `-1.045` n `238`; crypto_major avg `-0.618` n `8`; equity avg `-0.1592` n `156`; fx avg `0.0945` n `6`; index avg `-0.0532` n `27`; metal avg `-0.1754` n `20`; unknown avg `2.7805` n `1150`
- 24h: commodity avg `-0.5741` n `13`; crypto_alt avg `-2.0964` n `238`; crypto_major avg `-0.4631` n `8`; equity avg `1.0107` n `156`; fx avg `0.2837` n `6`; index avg `0.292` n `27`; metal avg `0.05` n `20`; unknown avg `4.8972` n `1063`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
