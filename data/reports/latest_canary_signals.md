# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T20:07:34.403878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0656` n `13`; crypto_alt avg `0.2527` n `235`; crypto_major avg `0.1776` n `8`; equity avg `0.3087` n `151`; fx avg `-0.0159` n `6`; index avg `0.0271` n `26`; metal avg `-0.0135` n `20`; unknown avg `0.84` n `1119`
- 1h: commodity avg `0.1391` n `13`; crypto_alt avg `0.1339` n `235`; crypto_major avg `-0.0406` n `8`; equity avg `0.3935` n `151`; fx avg `-0.0227` n `6`; index avg `0.0317` n `26`; metal avg `-0.0187` n `20`; unknown avg `78.2371` n `1103`
- 4h: commodity avg `0.3087` n `13`; crypto_alt avg `0.5725` n `235`; crypto_major avg `-0.0151` n `8`; equity avg `0.5809` n `151`; fx avg `-0.0013` n `6`; index avg `0.0787` n `26`; metal avg `0.0137` n `20`; unknown avg `3.1835` n `1103`
- 24h: commodity avg `0.8675` n `13`; crypto_alt avg `-1.3972` n `235`; crypto_major avg `-0.6285` n `8`; equity avg `-0.657` n `151`; fx avg `0.1605` n `6`; index avg `-0.1465` n `26`; metal avg `-0.2363` n `20`; unknown avg `1.0941` n `1002`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1583`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1423`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0922`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `666`, weak_sample_signal
