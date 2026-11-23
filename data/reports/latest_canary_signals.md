# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T02:22:29.214456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.022` n `13`; crypto_alt avg `-0.1339` n `239`; crypto_major avg `-0.0248` n `8`; equity avg `-0.4967` n `166`; fx avg `-0.0112` n `6`; index avg `-0.0635` n `27`; metal avg `-0.0497` n `20`; unknown avg `4.806` n `1263`
- 1h: commodity avg `-0.0231` n `13`; crypto_alt avg `-0.3608` n `239`; crypto_major avg `-0.3793` n `8`; equity avg `-0.2894` n `166`; fx avg `0.0396` n `6`; index avg `-0.051` n `27`; metal avg `-0.2485` n `20`; unknown avg `477.1681` n `1257`
- 4h: commodity avg `-0.3091` n `13`; crypto_alt avg `-0.3821` n `239`; crypto_major avg `-0.3538` n `8`; equity avg `0.1436` n `166`; fx avg `0.0954` n `6`; index avg `0.037` n `27`; metal avg `0.0835` n `20`; unknown avg `203.1895` n `1228`
- 24h: commodity avg `-0.4355` n `13`; crypto_alt avg `0.4165` n `239`; crypto_major avg `0.7092` n `8`; equity avg `0.9263` n `166`; fx avg `0.1925` n `6`; index avg `0.095` n `27`; metal avg `0.0992` n `20`; unknown avg `243.3577` n `1029`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
