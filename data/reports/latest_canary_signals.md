# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T11:07:38.872063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.18` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `0.1239` n `230`; crypto_major avg `0.1033` n `8`; equity avg `0.0207` n `102`; fx avg `-0.0014` n `6`; index avg `0.0415` n `25`; metal avg `0.0086` n `20`; unknown avg `0.1045` n `777`
- 1h: commodity avg `0.119` n `12`; crypto_alt avg `-0.2681` n `230`; crypto_major avg `-0.2197` n `8`; equity avg `-0.5749` n `102`; fx avg `0.0103` n `6`; index avg `-0.0249` n `25`; metal avg `-0.0536` n `20`; unknown avg `0.0158` n `777`
- 4h: commodity avg `0.2654` n `12`; crypto_alt avg `-0.1467` n `230`; crypto_major avg `-0.2015` n `8`; equity avg `0.2855` n `102`; fx avg `0.0345` n `6`; index avg `0.0674` n `25`; metal avg `-0.2263` n `20`; unknown avg `-0.0324` n `777`
- 24h: commodity avg `0.2231` n `12`; crypto_alt avg `-1.0734` n `230`; crypto_major avg `1.4013` n `8`; equity avg `-0.4266` n `102`; fx avg `-0.0517` n `6`; index avg `0.0282` n `25`; metal avg `0.0309` n `20`; unknown avg `-0.4764` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
