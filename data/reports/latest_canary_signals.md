# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T06:52:31.229080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.011` n `12`; crypto_alt avg `0.0113` n `234`; crypto_major avg `-0.0036` n `8`; equity avg `-0.0423` n `140`; fx avg `0.0216` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.1643` n `945`
- 1h: commodity avg `-0.0325` n `12`; crypto_alt avg `0.6766` n `234`; crypto_major avg `0.2668` n `8`; equity avg `0.099` n `140`; fx avg `0.0585` n `6`; index avg `0.0304` n `26`; metal avg `-0.012` n `20`; unknown avg `0.064` n `927`
- 4h: commodity avg `-0.0647` n `12`; crypto_alt avg `1.0092` n `234`; crypto_major avg `0.3954` n `8`; equity avg `0.1982` n `140`; fx avg `0.062` n `6`; index avg `0.0688` n `26`; metal avg `-0.037` n `20`; unknown avg `-0.0782` n `921`
- 24h: commodity avg `-0.188` n `12`; crypto_alt avg `4.0792` n `234`; crypto_major avg `2.0257` n `8`; equity avg `1.3697` n `140`; fx avg `-0.1239` n `6`; index avg `0.171` n `26`; metal avg `0.2164` n `20`; unknown avg `2.0424` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
