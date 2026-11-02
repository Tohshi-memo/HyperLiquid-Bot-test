# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T02:37:01.609903+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0667` n `13`; crypto_alt avg `-0.0708` n `238`; crypto_major avg `-0.1379` n `8`; equity avg `-0.0926` n `156`; fx avg `0.0212` n `6`; index avg `-0.018` n `27`; metal avg `-0.0759` n `20`; unknown avg `0.0648` n `1263`
- 1h: commodity avg `-0.1301` n `13`; crypto_alt avg `-0.2161` n `238`; crypto_major avg `-0.33` n `8`; equity avg `-0.1345` n `156`; fx avg `0.0624` n `6`; index avg `-0.0087` n `27`; metal avg `-0.0493` n `20`; unknown avg `1.3986` n `1253`
- 4h: commodity avg `-0.2818` n `13`; crypto_alt avg `0.4767` n `238`; crypto_major avg `0.8541` n `8`; equity avg `0.7011` n `156`; fx avg `0.1817` n `6`; index avg `0.2011` n `27`; metal avg `0.0581` n `20`; unknown avg `164.8035` n `1231`
- 24h: commodity avg `-0.233` n `13`; crypto_alt avg `-0.182` n `238`; crypto_major avg `0.454` n `8`; equity avg `0.9435` n `156`; fx avg `0.1699` n `6`; index avg `0.2765` n `27`; metal avg `0.0649` n `20`; unknown avg `3.2384` n `1120`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
