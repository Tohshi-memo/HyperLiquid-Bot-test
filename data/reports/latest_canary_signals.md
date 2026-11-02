# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T08:07:28.817545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0554` n `13`; crypto_alt avg `0.1244` n `238`; crypto_major avg `0.2588` n `8`; equity avg `0.078` n `156`; fx avg `-0.0186` n `6`; index avg `0.0132` n `27`; metal avg `-0.0125` n `20`; unknown avg `4.1105` n `1196`
- 1h: commodity avg `-0.0857` n `13`; crypto_alt avg `-0.0299` n `238`; crypto_major avg `0.1048` n `8`; equity avg `-0.0892` n `156`; fx avg `0.0092` n `6`; index avg `-0.002` n `27`; metal avg `-0.0151` n `20`; unknown avg `4.0263` n `1172`
- 4h: commodity avg `-0.0631` n `13`; crypto_alt avg `-1.1993` n `238`; crypto_major avg `-0.9268` n `8`; equity avg `-0.4298` n `156`; fx avg `0.0214` n `6`; index avg `-0.0227` n `27`; metal avg `0.0426` n `20`; unknown avg `0.003` n `1153`
- 24h: commodity avg `-0.498` n `13`; crypto_alt avg `-1.7836` n `238`; crypto_major avg `-0.2395` n `8`; equity avg `1.0003` n `156`; fx avg `0.2239` n `6`; index avg `0.3081` n `27`; metal avg `0.1089` n `20`; unknown avg `2.4042` n `1067`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1875`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
