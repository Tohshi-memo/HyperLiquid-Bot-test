# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T03:37:13.071670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `12`; crypto_alt avg `-0.2701` n `228`; crypto_major avg `-0.1243` n `8`; equity avg `-0.0709` n `65`; fx avg `0.0008` n `5`; index avg `-0.0074` n `23`; metal avg `-0.0357` n `18`; unknown avg `-0.2063` n `375`
- 1h: commodity avg `-0.0502` n `12`; crypto_alt avg `-0.1632` n `228`; crypto_major avg `-0.082` n `8`; equity avg `-0.0292` n `65`; fx avg `0.0025` n `5`; index avg `-0.0627` n `23`; metal avg `-0.0318` n `18`; unknown avg `-0.3712` n `375`
- 4h: commodity avg `-0.0201` n `12`; crypto_alt avg `1.1979` n `228`; crypto_major avg `0.9866` n `8`; equity avg `0.1347` n `65`; fx avg `-0.0134` n `5`; index avg `0.0733` n `23`; metal avg `0.2632` n `18`; unknown avg `0.0354` n `375`
- 24h: commodity avg `-0.2205` n `12`; crypto_alt avg `4.476` n `228`; crypto_major avg `2.688` n `8`; equity avg `3.7888` n `65`; fx avg `0.0902` n `5`; index avg `1.361` n `23`; metal avg `0.1267` n `18`; unknown avg `1.4788` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
