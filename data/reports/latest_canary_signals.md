# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T06:22:30.072848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `0.1751` n `238`; crypto_major avg `-0.1111` n `8`; equity avg `-0.0217` n `156`; fx avg `-0.0022` n `6`; index avg `-0.0006` n `27`; metal avg `0.003` n `20`; unknown avg `0.5252` n `1260`
- 1h: commodity avg `0.0356` n `13`; crypto_alt avg `0.3754` n `238`; crypto_major avg `0.0219` n `8`; equity avg `-0.0107` n `156`; fx avg `0.0077` n `6`; index avg `0.0114` n `27`; metal avg `0.0077` n `20`; unknown avg `-0.1504` n `1228`
- 4h: commodity avg `-0.0103` n `13`; crypto_alt avg `-0.5425` n `238`; crypto_major avg `-0.6063` n `8`; equity avg `-0.0155` n `156`; fx avg `-0.0004` n `6`; index avg `-0.0384` n `27`; metal avg `0.0101` n `20`; unknown avg `-0.2271` n `1210`
- 24h: commodity avg `0.0252` n `13`; crypto_alt avg `0.9612` n `238`; crypto_major avg `-1.8474` n `8`; equity avg `-2.5146` n `156`; fx avg `-0.0694` n `6`; index avg `-0.1929` n `27`; metal avg `-0.5296` n `20`; unknown avg `4.1377` n `1002`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
