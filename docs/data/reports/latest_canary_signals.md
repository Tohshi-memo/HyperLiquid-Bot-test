# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T19:52:27.080053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `13`; crypto_alt avg `0.087` n `238`; crypto_major avg `0.0014` n `8`; equity avg `-0.0122` n `156`; fx avg `-0.0143` n `6`; index avg `0.0006` n `27`; metal avg `-0.0044` n `20`; unknown avg `160.1147` n `1263`
- 1h: commodity avg `0.0318` n `13`; crypto_alt avg `-0.233` n `238`; crypto_major avg `-0.274` n `8`; equity avg `-0.0604` n `156`; fx avg `-0.0142` n `6`; index avg `-0.0249` n `27`; metal avg `-0.0265` n `20`; unknown avg `12.5437` n `1241`
- 4h: commodity avg `0.0694` n `13`; crypto_alt avg `-0.9503` n `238`; crypto_major avg `-0.5569` n `8`; equity avg `-0.2119` n `156`; fx avg `-0.0064` n `6`; index avg `-0.0387` n `27`; metal avg `-0.0278` n `20`; unknown avg `-0.0102` n `1219`
- 24h: commodity avg `0.1137` n `10`; crypto_alt avg `-0.88` n `231`; crypto_major avg `-0.4334` n `8`; equity avg `0.2455` n `118`; fx avg `0.0018` n `5`; index avg `0.1306` n `8`; metal avg `0.0364` n `16`; unknown avg `4.1851` n `959`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
