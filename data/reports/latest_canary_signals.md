# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T10:07:31.391778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.93` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1153` n `12`; crypto_alt avg `-0.0063` n `230`; crypto_major avg `-0.0288` n `8`; equity avg `-0.1322` n `102`; fx avg `-0.0038` n `6`; index avg `-0.0038` n `25`; metal avg `-0.0585` n `20`; unknown avg `0.0345` n `777`
- 1h: commodity avg `0.1425` n `12`; crypto_alt avg `0.1055` n `230`; crypto_major avg `0.1683` n `8`; equity avg `0.3093` n `102`; fx avg `-0.0189` n `6`; index avg `0.0602` n `25`; metal avg `-0.0578` n `20`; unknown avg `0.0796` n `777`
- 4h: commodity avg `0.0511` n `12`; crypto_alt avg `0.3374` n `230`; crypto_major avg `0.4559` n `8`; equity avg `1.7827` n `102`; fx avg `0.0174` n `6`; index avg `0.4516` n `25`; metal avg `-0.0958` n `20`; unknown avg `-0.1567` n `777`
- 24h: commodity avg `0.1927` n `12`; crypto_alt avg `-1.0805` n `230`; crypto_major avg `1.4061` n `8`; equity avg `-0.4077` n `102`; fx avg `-0.0626` n `6`; index avg `-0.0153` n `25`; metal avg `0.0882` n `20`; unknown avg `-0.5221` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
