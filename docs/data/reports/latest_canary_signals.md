# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T08:37:27.496921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `12`; crypto_alt avg `-0.0112` n `230`; crypto_major avg `0.0327` n `8`; equity avg `0.069` n `100`; fx avg `-0.0051` n `6`; index avg `0.0223` n `25`; metal avg `0.006` n `20`; unknown avg `-0.0657` n `775`
- 1h: commodity avg `-0.0834` n `12`; crypto_alt avg `-0.2131` n `230`; crypto_major avg `-0.0613` n `8`; equity avg `0.0244` n `100`; fx avg `0.0175` n `6`; index avg `0.0108` n `25`; metal avg `-0.0873` n `20`; unknown avg `-0.1133` n `775`
- 4h: commodity avg `-0.3202` n `12`; crypto_alt avg `-0.2703` n `230`; crypto_major avg `-0.0163` n `8`; equity avg `0.6019` n `100`; fx avg `0.0139` n `6`; index avg `0.1169` n `25`; metal avg `0.1229` n `20`; unknown avg `0.0086` n `759`
- 24h: commodity avg `-0.8184` n `12`; crypto_alt avg `0.5548` n `230`; crypto_major avg `1.3755` n `8`; equity avg `1.4728` n `100`; fx avg `0.1259` n `6`; index avg `0.1844` n `25`; metal avg `0.4236` n `20`; unknown avg `-0.0684` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
