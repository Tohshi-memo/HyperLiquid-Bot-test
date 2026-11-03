# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T20:24:06.147473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0336` n `13`; crypto_alt avg `-0.0869` n `239`; crypto_major avg `-0.0761` n `8`; equity avg `0.0758` n `158`; fx avg `-0.0012` n `6`; index avg `0.0185` n `27`; metal avg `0.0205` n `20`; unknown avg `-0.0441` n `1261`
- 1h: commodity avg `0.159` n `13`; crypto_alt avg `-0.256` n `239`; crypto_major avg `-0.1355` n `8`; equity avg `0.0774` n `158`; fx avg `-0.0118` n `6`; index avg `-0.0142` n `27`; metal avg `-0.0266` n `20`; unknown avg `25.8186` n `1235`
- 4h: commodity avg `0.2641` n `13`; crypto_alt avg `-0.0747` n `239`; crypto_major avg `-0.0422` n `8`; equity avg `-0.0828` n `158`; fx avg `0.0207` n `6`; index avg `-0.0257` n `27`; metal avg `-0.1458` n `20`; unknown avg `0.0073` n `1201`
- 24h: commodity avg `0.3678` n `13`; crypto_alt avg `0.8035` n `239`; crypto_major avg `1.1774` n `8`; equity avg `1.1865` n `158`; fx avg `0.0774` n `6`; index avg `0.0942` n `27`; metal avg `-0.5389` n `20`; unknown avg `392.4443` n `1061`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
