# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T10:15:38.241748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0478` n `12`; crypto_alt avg `0.1211` n `228`; crypto_major avg `0.0082` n `8`; equity avg `-0.0085` n `65`; fx avg `0.0042` n `5`; index avg `0.0002` n `23`; metal avg `-0.0102` n `18`; unknown avg `-0.0998` n `376`
- 1h: commodity avg `-0.0463` n `12`; crypto_alt avg `-0.1921` n `228`; crypto_major avg `-0.2434` n `8`; equity avg `0.0202` n `65`; fx avg `0.0042` n `5`; index avg `-0.0714` n `23`; metal avg `-0.0337` n `18`; unknown avg `0.0192` n `376`
- 4h: commodity avg `-0.0362` n `12`; crypto_alt avg `-1.1151` n `228`; crypto_major avg `-0.4752` n `8`; equity avg `0.0567` n `65`; fx avg `0.0051` n `5`; index avg `0.0313` n `23`; metal avg `-0.0362` n `18`; unknown avg `-0.0569` n `376`
- 24h: commodity avg `-0.2768` n `12`; crypto_alt avg `3.1018` n `228`; crypto_major avg `2.0805` n `8`; equity avg `2.7739` n `65`; fx avg `-0.0457` n `5`; index avg `1.1525` n `23`; metal avg `-0.1406` n `18`; unknown avg `0.4527` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
