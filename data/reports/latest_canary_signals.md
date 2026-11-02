# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T03:07:27.047145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0449` n `13`; crypto_alt avg `0.1363` n `238`; crypto_major avg `0.1281` n `8`; equity avg `0.1938` n `156`; fx avg `0.0171` n `6`; index avg `0.0266` n `27`; metal avg `0.0933` n `20`; unknown avg `-0.2269` n `1257`
- 1h: commodity avg `-0.1771` n `13`; crypto_alt avg `0.0641` n `238`; crypto_major avg `0.0879` n `8`; equity avg `0.2961` n `156`; fx avg `0.0643` n `6`; index avg `0.0181` n `27`; metal avg `-0.0853` n `20`; unknown avg `1.2203` n `1257`
- 4h: commodity avg `-0.2832` n `13`; crypto_alt avg `0.2329` n `238`; crypto_major avg `0.8117` n `8`; equity avg `1.0304` n `156`; fx avg `0.1683` n `6`; index avg `0.2593` n `27`; metal avg `0.007` n `20`; unknown avg `2.5795` n `1241`
- 24h: commodity avg `-0.3422` n `13`; crypto_alt avg `-0.2589` n `238`; crypto_major avg `0.5165` n `8`; equity avg `1.0845` n `156`; fx avg `0.1786` n `6`; index avg `0.2698` n `27`; metal avg `0.0544` n `20`; unknown avg `3.218` n `1122`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1855`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1774`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
