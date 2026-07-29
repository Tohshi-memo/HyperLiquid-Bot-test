# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T09:07:38.446670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.72` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0571` n `12`; crypto_alt avg `0.0549` n `230`; crypto_major avg `0.0335` n `8`; equity avg `0.4114` n `102`; fx avg `-0.0043` n `6`; index avg `0.0226` n `25`; metal avg `-0.0188` n `20`; unknown avg `-0.0372` n `777`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `-0.0962` n `230`; crypto_major avg `-0.143` n `8`; equity avg `0.5282` n `102`; fx avg `0.0156` n `6`; index avg `0.0324` n `25`; metal avg `-0.0851` n `20`; unknown avg `-0.049` n `777`
- 4h: commodity avg `0.0087` n `12`; crypto_alt avg `0.2916` n `230`; crypto_major avg `0.4282` n `8`; equity avg `1.4717` n `102`; fx avg `0.0927` n `6`; index avg `0.4089` n `25`; metal avg `0.0549` n `20`; unknown avg `-0.1722` n `761`
- 24h: commodity avg `0.0714` n `12`; crypto_alt avg `-1.0901` n `230`; crypto_major avg `1.1184` n `8`; equity avg `-0.9632` n `102`; fx avg `-0.1013` n `6`; index avg `-0.1297` n `25`; metal avg `-0.0781` n `20`; unknown avg `-0.6034` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
