# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T13:51:56.783257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0195` n `12`; crypto_alt avg `0.0156` n `228`; crypto_major avg `-0.0291` n `8`; equity avg `-0.0098` n `65`; fx avg `0.0` n `5`; index avg `0.0027` n `23`; metal avg `0.0001` n `18`; unknown avg `-0.0056` n `376`
- 1h: commodity avg `0.0385` n `12`; crypto_alt avg `-0.4043` n `228`; crypto_major avg `-0.1832` n `8`; equity avg `0.0033` n `65`; fx avg `-0.0127` n `5`; index avg `0.0503` n `23`; metal avg `-0.0271` n `18`; unknown avg `0.0064` n `376`
- 4h: commodity avg `0.0506` n `12`; crypto_alt avg `-0.1701` n `228`; crypto_major avg `-0.0837` n `8`; equity avg `0.1293` n `65`; fx avg `-0.0163` n `5`; index avg `0.0186` n `23`; metal avg `-0.0432` n `18`; unknown avg `-0.288` n `376`
- 24h: commodity avg `0.0038` n `12`; crypto_alt avg `2.8255` n `228`; crypto_major avg `2.1198` n `8`; equity avg `2.2231` n `65`; fx avg `0.0011` n `5`; index avg `0.6194` n `23`; metal avg `-0.4613` n `18`; unknown avg `0.2074` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
