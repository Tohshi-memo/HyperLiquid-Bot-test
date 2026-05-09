# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T12:37:16.575558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `-0.078` n `228`; crypto_major avg `-0.1108` n `8`; equity avg `0.0939` n `65`; fx avg `0.0` n `5`; index avg `0.0034` n `23`; metal avg `-0.0078` n `18`; unknown avg `-0.0106` n `376`
- 1h: commodity avg `0.037` n `12`; crypto_alt avg `-0.2914` n `228`; crypto_major avg `-0.0882` n `8`; equity avg `0.0693` n `65`; fx avg `-0.0134` n `5`; index avg `-0.0066` n `23`; metal avg `0.0132` n `18`; unknown avg `-0.0534` n `376`
- 4h: commodity avg `-0.0476` n `12`; crypto_alt avg `-0.6426` n `228`; crypto_major avg `-0.3358` n `8`; equity avg `0.0101` n `65`; fx avg `-0.0045` n `5`; index avg `-0.0749` n `23`; metal avg `-0.0166` n `18`; unknown avg `-0.482` n `376`
- 24h: commodity avg `-0.1297` n `12`; crypto_alt avg `3.088` n `228`; crypto_major avg `1.859` n `8`; equity avg `2.6211` n `65`; fx avg `-0.0134` n `5`; index avg `0.9003` n `23`; metal avg `-0.3816` n `18`; unknown avg `0.2539` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
