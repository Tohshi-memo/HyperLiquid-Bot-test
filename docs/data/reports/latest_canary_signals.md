# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T18:07:26.772926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0153` n `13`; crypto_alt avg `-0.0243` n `238`; crypto_major avg `-0.0426` n `8`; equity avg `-0.0112` n `156`; fx avg `-0.005` n `6`; index avg `-0.0003` n `27`; metal avg `-0.0025` n `20`; unknown avg `158.9859` n `1257`
- 1h: commodity avg `0.0054` n `13`; crypto_alt avg `-0.1065` n `238`; crypto_major avg `-0.0878` n `8`; equity avg `-0.0585` n `156`; fx avg `0.0022` n `6`; index avg `-0.0019` n `27`; metal avg `-0.0056` n `20`; unknown avg `158.8109` n `1257`
- 4h: commodity avg `-0.0622` n `13`; crypto_alt avg `-0.6957` n `238`; crypto_major avg `-0.2963` n `8`; equity avg `-0.0209` n `156`; fx avg `0.0025` n `6`; index avg `0.0407` n `27`; metal avg `-0.0011` n `20`; unknown avg `-0.1434` n `1245`
- 24h: commodity avg `0.0164` n `13`; crypto_alt avg `-0.4196` n `238`; crypto_major avg `-0.1006` n `8`; equity avg `0.4026` n `156`; fx avg `0.0129` n `6`; index avg `0.0926` n `27`; metal avg `0.0571` n `20`; unknown avg `3.4449` n `1012`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
