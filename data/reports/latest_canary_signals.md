# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T08:37:14.830172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.033` n `12`; crypto_alt avg `-0.0095` n `228`; crypto_major avg `0.0339` n `8`; equity avg `0.0288` n `65`; fx avg `0.0` n `5`; index avg `0.0215` n `23`; metal avg `-0.0023` n `18`; unknown avg `-0.0125` n `376`
- 1h: commodity avg `-0.0216` n `12`; crypto_alt avg `0.2231` n `228`; crypto_major avg `0.0862` n `8`; equity avg `0.1757` n `65`; fx avg `0.0006` n `5`; index avg `0.0297` n `23`; metal avg `-0.0153` n `18`; unknown avg `-0.0489` n `376`
- 4h: commodity avg `0.0356` n `12`; crypto_alt avg `-0.2777` n `228`; crypto_major avg `-0.1484` n `8`; equity avg `0.1644` n `65`; fx avg `0.0198` n `5`; index avg `0.056` n `23`; metal avg `-0.0003` n `18`; unknown avg `-0.3118` n `355`
- 24h: commodity avg `0.0761` n `12`; crypto_alt avg `4.0751` n `228`; crypto_major avg `2.4869` n `8`; equity avg `2.9037` n `65`; fx avg `0.003` n `5`; index avg `1.2228` n `23`; metal avg `-0.1417` n `18`; unknown avg `0.488` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
