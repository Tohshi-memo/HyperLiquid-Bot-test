# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T19:07:17.832931+00:00`
- Correlation status: `ready`
- Asset price records: `576`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0195` n `12`; crypto_alt avg `-0.0664` n `228`; crypto_major avg `0.0249` n `8`; equity avg `0.0983` n `65`; fx avg `-0.0112` n `5`; index avg `0.1528` n `23`; metal avg `0.2153` n `18`; unknown avg `-0.2197` n `365`
- 1h: commodity avg `0.4753` n `12`; crypto_alt avg `-0.2332` n `228`; crypto_major avg `-0.3483` n `8`; equity avg `-0.3979` n `65`; fx avg `0.0104` n `5`; index avg `-0.2366` n `23`; metal avg `-0.3434` n `18`; unknown avg `-0.1662` n `365`
- 4h: commodity avg `1.4933` n `12`; crypto_alt avg `0.7423` n `228`; crypto_major avg `-0.2878` n `8`; equity avg `-1.4427` n `65`; fx avg `0.0466` n `5`; index avg `-0.8774` n `23`; metal avg `-1.6009` n `18`; unknown avg `-0.1721` n `365`
- 24h: commodity avg `0.6679` n `12`; crypto_alt avg `1.0496` n `228`; crypto_major avg `-1.8915` n `8`; equity avg `-1.1452` n `65`; fx avg `0.1845` n `5`; index avg `-0.7866` n `23`; metal avg `0.2467` n `18`; unknown avg `-0.1012` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1393`, n `572`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.117`, n `572`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `572`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `572`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `568`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `568`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0927`, n `568`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0881`, n `568`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0874`, n `568`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.083`, n `568`, weak_sample_signal
