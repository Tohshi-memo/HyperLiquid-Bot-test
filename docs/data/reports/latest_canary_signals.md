# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T12:25:29.749142+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.25` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.3476` n `12`; crypto_alt avg `-0.1005` n `230`; crypto_major avg `-0.172` n `8`; equity avg `-0.3816` n `102`; fx avg `0.0067` n `6`; index avg `-0.1083` n `25`; metal avg `-0.2038` n `20`; unknown avg `0.0417` n `777`
- 1h: commodity avg `0.2352` n `12`; crypto_alt avg `-0.2555` n `230`; crypto_major avg `-0.3182` n `8`; equity avg `-0.5536` n `102`; fx avg `-0.0058` n `6`; index avg `-0.2099` n `25`; metal avg `-0.1984` n `20`; unknown avg `0.4004` n `777`
- 4h: commodity avg `0.5225` n `12`; crypto_alt avg `-0.3347` n `230`; crypto_major avg `-0.2631` n `8`; equity avg `0.272` n `102`; fx avg `0.0083` n `6`; index avg `-0.0136` n `25`; metal avg `-0.2946` n `20`; unknown avg `0.1919` n `777`
- 24h: commodity avg `0.4098` n `12`; crypto_alt avg `-1.5987` n `230`; crypto_major avg `0.9221` n `8`; equity avg `-0.9467` n `102`; fx avg `-0.0678` n `6`; index avg `-0.2155` n `25`; metal avg `-0.2352` n `20`; unknown avg `0.084` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
