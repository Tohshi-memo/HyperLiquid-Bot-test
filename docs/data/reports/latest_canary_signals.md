# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T10:52:27.884899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.18` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0758` n `12`; crypto_alt avg `-0.2836` n `230`; crypto_major avg `-0.1894` n `8`; equity avg `-0.2631` n `102`; fx avg `0.0053` n `6`; index avg `-0.0264` n `25`; metal avg `-0.05` n `20`; unknown avg `-0.0655` n `777`
- 1h: commodity avg `0.243` n `12`; crypto_alt avg `-0.3972` n `230`; crypto_major avg `-0.3513` n `8`; equity avg `-0.7255` n `102`; fx avg `0.0079` n `6`; index avg `-0.07` n `25`; metal avg `-0.1206` n `20`; unknown avg `-0.0218` n `777`
- 4h: commodity avg `0.2722` n `12`; crypto_alt avg `-0.2816` n `230`; crypto_major avg `-0.3074` n `8`; equity avg `0.2812` n `102`; fx avg `0.0444` n `6`; index avg `0.0515` n `25`; metal avg `-0.2226` n `20`; unknown avg `-0.1288` n `777`
- 24h: commodity avg `0.2465` n `12`; crypto_alt avg `-1.5043` n `230`; crypto_major avg `1.0293` n `8`; equity avg `-0.7827` n `102`; fx avg `-0.0518` n `6`; index avg `-0.0407` n `25`; metal avg `0.0142` n `20`; unknown avg `-0.4981` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
