# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T08:22:14.753744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `0.0926` n `228`; crypto_major avg `0.0079` n `8`; equity avg `0.0222` n `65`; fx avg `0.0` n `5`; index avg `0.0463` n `23`; metal avg `-0.0001` n `18`; unknown avg `0.0058` n `376`
- 1h: commodity avg `-0.0125` n `12`; crypto_alt avg `0.0861` n `228`; crypto_major avg `0.0107` n `8`; equity avg `0.1161` n `65`; fx avg `0.0006` n `5`; index avg `0.0165` n `23`; metal avg `-0.0027` n `18`; unknown avg `0.1069` n `376`
- 4h: commodity avg `-0.0141` n `12`; crypto_alt avg `-0.2311` n `228`; crypto_major avg `-0.2246` n `8`; equity avg `0.0995` n `65`; fx avg `0.0198` n `5`; index avg `0.0362` n `23`; metal avg `-0.0021` n `18`; unknown avg `-0.2984` n `355`
- 24h: commodity avg `-0.116` n `12`; crypto_alt avg `4.1965` n `228`; crypto_major avg `2.5413` n `8`; equity avg `2.9255` n `65`; fx avg `0.0054` n `5`; index avg `1.223` n `23`; metal avg `-0.1403` n `18`; unknown avg `0.9571` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
