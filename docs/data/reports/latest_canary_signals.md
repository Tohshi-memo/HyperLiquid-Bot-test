# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T12:22:29.157445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.3166` n `12`; crypto_alt avg `-0.199` n `230`; crypto_major avg `-0.2449` n `8`; equity avg `-0.4646` n `102`; fx avg `0.0119` n `6`; index avg `-0.1289` n `25`; metal avg `-0.1738` n `20`; unknown avg `0.034` n `777`
- 1h: commodity avg `0.2043` n `12`; crypto_alt avg `-0.354` n `230`; crypto_major avg `-0.391` n `8`; equity avg `-0.6361` n `102`; fx avg `-0.0005` n `6`; index avg `-0.2304` n `25`; metal avg `-0.1684` n `20`; unknown avg `0.3929` n `777`
- 4h: commodity avg `0.4911` n `12`; crypto_alt avg `-0.4328` n `230`; crypto_major avg `-0.3359` n `8`; equity avg `0.188` n `102`; fx avg `0.0135` n `6`; index avg `-0.0343` n `25`; metal avg `-0.2648` n `20`; unknown avg `0.1824` n `777`
- 24h: commodity avg `0.378` n `12`; crypto_alt avg `-1.694` n `230`; crypto_major avg `0.8484` n `8`; equity avg `-1.0285` n `102`; fx avg `-0.0626` n `6`; index avg `-0.2359` n `25`; metal avg `-0.2053` n `20`; unknown avg `0.0726` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
