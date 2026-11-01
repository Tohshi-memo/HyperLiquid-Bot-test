# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T06:37:23.731943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0188` n `13`; crypto_alt avg `-0.1373` n `238`; crypto_major avg `-0.0766` n `8`; equity avg `0.0096` n `156`; fx avg `-0.0011` n `6`; index avg `0.003` n `27`; metal avg `0.0247` n `20`; unknown avg `0.0448` n `1261`
- 1h: commodity avg `-0.0307` n `13`; crypto_alt avg `0.1164` n `238`; crypto_major avg `-0.0142` n `8`; equity avg `0.0826` n `156`; fx avg `0.0097` n `6`; index avg `0.0094` n `27`; metal avg `0.0276` n `20`; unknown avg `0.5678` n `1238`
- 4h: commodity avg `0.0669` n `13`; crypto_alt avg `0.6357` n `238`; crypto_major avg `0.2328` n `8`; equity avg `0.2811` n `156`; fx avg `0.0024` n `6`; index avg `0.0395` n `27`; metal avg `0.027` n `20`; unknown avg `0.8759` n `1226`
- 24h: commodity avg `-0.0229` n `13`; crypto_alt avg `0.4549` n `238`; crypto_major avg `0.2944` n `8`; equity avg `0.3171` n `156`; fx avg `0.0086` n `6`; index avg `0.0022` n `27`; metal avg `0.0485` n `20`; unknown avg `2.0462` n `996`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
