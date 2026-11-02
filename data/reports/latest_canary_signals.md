# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T09:52:36.046968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0088` n `13`; crypto_alt avg `0.1287` n `238`; crypto_major avg `0.1208` n `8`; equity avg `0.1283` n `156`; fx avg `-0.0031` n `6`; index avg `0.0108` n `27`; metal avg `-0.0311` n `20`; unknown avg `0.0594` n `1264`
- 1h: commodity avg `-0.0296` n `13`; crypto_alt avg `-0.1949` n `238`; crypto_major avg `-0.2272` n `8`; equity avg `0.141` n `156`; fx avg `0.0036` n `6`; index avg `0.0274` n `27`; metal avg `-0.1298` n `20`; unknown avg `2.0602` n `1256`
- 4h: commodity avg `-0.1723` n `13`; crypto_alt avg `-0.9823` n `238`; crypto_major avg `-0.5494` n `8`; equity avg `-0.1283` n `156`; fx avg `0.0945` n `6`; index avg `-0.0374` n `27`; metal avg `-0.1756` n `20`; unknown avg `2.8559` n `1152`
- 24h: commodity avg `-0.5716` n `13`; crypto_alt avg `-2.0345` n `238`; crypto_major avg `-0.3945` n `8`; equity avg `1.0427` n `156`; fx avg `0.2837` n `6`; index avg `0.3083` n `27`; metal avg `0.0498` n `20`; unknown avg `5.0417` n `1065`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
