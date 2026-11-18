# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T13:52:28.935067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.5` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0728` n `13`; crypto_alt avg `-0.1228` n `239`; crypto_major avg `-0.221` n `8`; equity avg `0.0217` n `163`; fx avg `-0.0031` n `6`; index avg `0.0101` n `27`; metal avg `0.0461` n `20`; unknown avg `1.2599` n `1266`
- 1h: commodity avg `0.1761` n `13`; crypto_alt avg `0.1989` n `239`; crypto_major avg `-0.1115` n `8`; equity avg `0.1474` n `163`; fx avg `0.0268` n `6`; index avg `0.0283` n `27`; metal avg `0.208` n `20`; unknown avg `2.4892` n `1264`
- 4h: commodity avg `0.3571` n `13`; crypto_alt avg `-0.2155` n `239`; crypto_major avg `-0.7885` n `8`; equity avg `-0.7031` n `163`; fx avg `0.0143` n `6`; index avg `-0.0825` n `27`; metal avg `-0.0413` n `20`; unknown avg `4.3336` n `1256`
- 24h: commodity avg `-0.0301` n `13`; crypto_alt avg `-0.0812` n `239`; crypto_major avg `-0.4555` n `8`; equity avg `0.0406` n `163`; fx avg `-0.09` n `6`; index avg `0.0159` n `27`; metal avg `-0.8999` n `20`; unknown avg `74.906` n `1137`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
