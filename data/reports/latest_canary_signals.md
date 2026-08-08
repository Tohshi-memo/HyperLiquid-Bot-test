# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T13:22:35.628107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0279` n `12`; crypto_alt avg `-0.0673` n `230`; crypto_major avg `-0.1053` n `8`; equity avg `0.1594` n `112`; fx avg `-0.002` n `6`; index avg `0.0258` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.0964` n `784`
- 1h: commodity avg `0.0398` n `12`; crypto_alt avg `0.0172` n `230`; crypto_major avg `0.0442` n `8`; equity avg `0.1644` n `112`; fx avg `-0.0025` n `6`; index avg `0.0338` n `25`; metal avg `0.0018` n `20`; unknown avg `-0.1331` n `784`
- 4h: commodity avg `0.0971` n `12`; crypto_alt avg `0.241` n `230`; crypto_major avg `0.1555` n `8`; equity avg `0.2872` n `112`; fx avg `-0.0156` n `6`; index avg `0.0371` n `25`; metal avg `-0.0192` n `20`; unknown avg `-0.0905` n `784`
- 24h: commodity avg `0.0271` n `12`; crypto_alt avg `0.2369` n `230`; crypto_major avg `-0.1552` n `8`; equity avg `0.1442` n `112`; fx avg `0.0185` n `6`; index avg `-0.0392` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.1301` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
