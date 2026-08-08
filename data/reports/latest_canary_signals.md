# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T14:08:09.242167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.0377` n `230`; crypto_major avg `0.0725` n `8`; equity avg `0.0456` n `112`; fx avg `0.0013` n `6`; index avg `-0.0037` n `25`; metal avg `0.0009` n `20`; unknown avg `-0.0312` n `784`
- 1h: commodity avg `0.0479` n `12`; crypto_alt avg `-0.0188` n `230`; crypto_major avg `0.0108` n `8`; equity avg `0.1533` n `112`; fx avg `0.0` n `6`; index avg `0.0095` n `25`; metal avg `-0.0028` n `20`; unknown avg `-0.2197` n `784`
- 4h: commodity avg `0.1221` n `12`; crypto_alt avg `0.2494` n `230`; crypto_major avg `0.2625` n `8`; equity avg `0.2477` n `112`; fx avg `-0.011` n `6`; index avg `0.0321` n `25`; metal avg `-0.0435` n `20`; unknown avg `-0.2609` n `784`
- 24h: commodity avg `-0.0997` n `12`; crypto_alt avg `0.4786` n `230`; crypto_major avg `0.4632` n `8`; equity avg `1.367` n `112`; fx avg `-0.0005` n `6`; index avg `0.0771` n `25`; metal avg `0.1247` n `20`; unknown avg `-0.0953` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
