# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T03:22:19.404139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0324` n `12`; crypto_alt avg `0.1145` n `228`; crypto_major avg `0.1447` n `8`; equity avg `0.0176` n `65`; fx avg `-0.0006` n `5`; index avg `0.0061` n `23`; metal avg `-0.0299` n `18`; unknown avg `1.0696` n `375`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `0.0878` n `228`; crypto_major avg `0.1256` n `8`; equity avg `0.0913` n `65`; fx avg `-0.0255` n `5`; index avg `-0.0035` n `23`; metal avg `0.0697` n `18`; unknown avg `0.2403` n `375`
- 4h: commodity avg `0.012` n `12`; crypto_alt avg `1.2755` n `228`; crypto_major avg `0.955` n `8`; equity avg `0.1907` n `65`; fx avg `-0.0159` n `5`; index avg `0.1283` n `23`; metal avg `0.2517` n `18`; unknown avg `0.4784` n `375`
- 24h: commodity avg `-0.2798` n `12`; crypto_alt avg `4.8958` n `228`; crypto_major avg `2.887` n `8`; equity avg `3.9362` n `65`; fx avg `0.0967` n `5`; index avg `1.4114` n `23`; metal avg `0.3883` n `18`; unknown avg `1.7287` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
