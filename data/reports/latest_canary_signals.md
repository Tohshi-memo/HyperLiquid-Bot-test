# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T12:07:28.033914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.25` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0345` n `12`; crypto_alt avg `-0.0908` n `230`; crypto_major avg `-0.0884` n `8`; equity avg `-0.0083` n `102`; fx avg `-0.0155` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0158` n `20`; unknown avg `0.2202` n `777`
- 1h: commodity avg `-0.1265` n `12`; crypto_alt avg `-0.1592` n `230`; crypto_major avg `-0.131` n `8`; equity avg `0.1667` n `102`; fx avg `-0.0078` n `6`; index avg `-0.0119` n `25`; metal avg `0.0466` n `20`; unknown avg `0.3544` n `777`
- 4h: commodity avg `0.1531` n `12`; crypto_alt avg `-0.4173` n `230`; crypto_major avg `-0.3258` n `8`; equity avg `0.4112` n `102`; fx avg `-0.0008` n `6`; index avg `0.0558` n `25`; metal avg `-0.1498` n `20`; unknown avg `0.2253` n `777`
- 24h: commodity avg `0.0537` n `12`; crypto_alt avg `-1.3875` n `230`; crypto_major avg `1.1426` n `8`; equity avg `-0.4292` n `102`; fx avg `-0.0747` n `6`; index avg `-0.0795` n `25`; metal avg `0.0219` n `20`; unknown avg `0.0225` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
