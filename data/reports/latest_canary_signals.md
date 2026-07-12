# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T13:22:24.392460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `-0.0193` n `230`; crypto_major avg `-0.0339` n `8`; equity avg `0.0199` n `92`; fx avg `0.0001` n `6`; index avg `-0.0017` n `25`; metal avg `0.0019` n `20`; unknown avg `0.0037` n `765`
- 1h: commodity avg `0.0213` n `12`; crypto_alt avg `-0.0581` n `230`; crypto_major avg `0.085` n `8`; equity avg `0.0333` n `92`; fx avg `-0.0028` n `6`; index avg `-0.0068` n `25`; metal avg `0.0082` n `20`; unknown avg `-0.0606` n `765`
- 4h: commodity avg `-0.0534` n `12`; crypto_alt avg `0.347` n `230`; crypto_major avg `0.7373` n `8`; equity avg `0.1125` n `92`; fx avg `0.0006` n `6`; index avg `-0.006` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.0496` n `763`
- 24h: commodity avg `0.4209` n `12`; crypto_alt avg `-0.996` n `230`; crypto_major avg `-0.413` n `8`; equity avg `-0.0026` n `92`; fx avg `0.0116` n `6`; index avg `-0.122` n `25`; metal avg `-0.0941` n `20`; unknown avg `0.1137` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
