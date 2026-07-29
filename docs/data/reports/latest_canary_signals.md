# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T09:52:33.214733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.9` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0458` n `12`; crypto_alt avg `-0.0692` n `230`; crypto_major avg `0.0223` n `8`; equity avg `0.3902` n `102`; fx avg `-0.0073` n `6`; index avg `0.0709` n `25`; metal avg `0.0117` n `20`; unknown avg `-0.0027` n `777`
- 1h: commodity avg `0.0843` n `12`; crypto_alt avg `0.1666` n `230`; crypto_major avg `0.2306` n `8`; equity avg `0.8534` n `102`; fx avg `-0.0193` n `6`; index avg `0.0867` n `25`; metal avg `-0.0181` n `20`; unknown avg `0.0038` n `777`
- 4h: commodity avg `0.0061` n `12`; crypto_alt avg `0.2182` n `230`; crypto_major avg `0.3849` n `8`; equity avg `1.5216` n `102`; fx avg `0.0328` n `6`; index avg `0.3653` n `25`; metal avg `-0.0238` n `20`; unknown avg `-0.1753` n `761`
- 24h: commodity avg `0.1098` n `12`; crypto_alt avg `-1.1572` n `230`; crypto_major avg `1.1788` n `8`; equity avg `-0.3419` n `102`; fx avg `-0.0749` n `6`; index avg `-0.0332` n `25`; metal avg `0.0843` n `20`; unknown avg `-0.5809` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
