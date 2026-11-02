# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T11:37:30.838990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `13`; crypto_alt avg `-0.0058` n `238`; crypto_major avg `0.0504` n `8`; equity avg `-0.0708` n `156`; fx avg `0.0011` n `6`; index avg `-0.0102` n `27`; metal avg `-0.0186` n `20`; unknown avg `28.8158` n `1264`
- 1h: commodity avg `-0.0934` n `13`; crypto_alt avg `0.1009` n `238`; crypto_major avg `0.0152` n `8`; equity avg `-0.0137` n `156`; fx avg `0.0028` n `6`; index avg `0.0045` n `27`; metal avg `0.0028` n `20`; unknown avg `-0.0238` n `1258`
- 4h: commodity avg `-0.1684` n `13`; crypto_alt avg `-0.1709` n `238`; crypto_major avg `0.0275` n `8`; equity avg `0.0076` n `156`; fx avg `0.0223` n `6`; index avg `0.0058` n `27`; metal avg `-0.0577` n `20`; unknown avg `7.5758` n `1170`
- 24h: commodity avg `-0.5422` n `13`; crypto_alt avg `-2.1259` n `238`; crypto_major avg `-0.6126` n `8`; equity avg `0.8377` n `156`; fx avg `0.273` n `6`; index avg `0.2876` n `27`; metal avg `0.0281` n `20`; unknown avg `3.8309` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
