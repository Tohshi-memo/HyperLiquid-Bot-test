# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T10:37:30.989941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `-0.0081` n `230`; crypto_major avg `-0.1372` n `8`; equity avg `-0.096` n `93`; fx avg `-0.0116` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0145` n `20`; unknown avg `-0.0948` n `767`
- 1h: commodity avg `0.0403` n `12`; crypto_alt avg `-0.0338` n `230`; crypto_major avg `-0.2369` n `8`; equity avg `-0.1201` n `93`; fx avg `-0.0179` n `6`; index avg `-0.0327` n `25`; metal avg `-0.0573` n `20`; unknown avg `-0.0912` n `767`
- 4h: commodity avg `0.1143` n `12`; crypto_alt avg `-0.2181` n `230`; crypto_major avg `-0.4594` n `8`; equity avg `-0.3155` n `93`; fx avg `-0.0011` n `6`; index avg `-0.0942` n `25`; metal avg `-0.0441` n `20`; unknown avg `-0.0797` n `765`
- 24h: commodity avg `-0.02` n `12`; crypto_alt avg `1.7993` n `230`; crypto_major avg `3.1423` n `8`; equity avg `1.0097` n `92`; fx avg `0.0019` n `6`; index avg `0.3577` n `25`; metal avg `0.2581` n `20`; unknown avg `0.2725` n `738`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
