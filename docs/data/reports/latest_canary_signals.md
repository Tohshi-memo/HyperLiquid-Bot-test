# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T19:23:46.695989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `0.0102` n `239`; crypto_major avg `0.057` n `8`; equity avg `-0.036` n `158`; fx avg `0.0029` n `6`; index avg `0.0042` n `27`; metal avg `-0.0304` n `20`; unknown avg `1.8881` n `1263`
- 1h: commodity avg `0.0607` n `13`; crypto_alt avg `0.0305` n `239`; crypto_major avg `-0.2161` n `8`; equity avg `-0.2231` n `158`; fx avg `0.015` n `6`; index avg `-0.0217` n `27`; metal avg `-0.0731` n `20`; unknown avg `0.6306` n `1257`
- 4h: commodity avg `0.0496` n `13`; crypto_alt avg `0.212` n `239`; crypto_major avg `0.0666` n `8`; equity avg `-0.2409` n `158`; fx avg `0.0498` n `6`; index avg `-0.0164` n `27`; metal avg `-0.1046` n `20`; unknown avg `-0.5281` n `1215`
- 24h: commodity avg `0.1671` n `13`; crypto_alt avg `1.2906` n `239`; crypto_major avg `1.5475` n `8`; equity avg `1.1263` n `158`; fx avg `0.086` n `6`; index avg `0.0912` n `27`; metal avg `-0.5422` n `20`; unknown avg `371.1993` n `1059`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
