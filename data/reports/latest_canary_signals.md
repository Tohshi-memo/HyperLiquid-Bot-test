# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T11:22:33.063162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.2` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0155` n `12`; crypto_alt avg `-0.0042` n `230`; crypto_major avg `0.0155` n `8`; equity avg `0.3413` n `102`; fx avg `0.0046` n `6`; index avg `0.0924` n `25`; metal avg `0.0412` n `20`; unknown avg `-0.0009` n `777`
- 1h: commodity avg `0.0893` n `12`; crypto_alt avg `-0.2395` n `230`; crypto_major avg `-0.1776` n `8`; equity avg `-0.1216` n `102`; fx avg `0.0163` n `6`; index avg `0.0731` n `25`; metal avg `0.0047` n `20`; unknown avg `0.0602` n `777`
- 4h: commodity avg `0.2114` n `12`; crypto_alt avg `-0.1238` n `230`; crypto_major avg `-0.108` n `8`; equity avg `0.4525` n `102`; fx avg `0.0447` n `6`; index avg `0.174` n `25`; metal avg `-0.1911` n `20`; unknown avg `-0.1388` n `777`
- 24h: commodity avg `0.2605` n `12`; crypto_alt avg `-1.3076` n `230`; crypto_major avg `1.2661` n `8`; equity avg `-0.1711` n `102`; fx avg `-0.0524` n `6`; index avg `0.086` n `25`; metal avg `0.0457` n `20`; unknown avg `-0.451` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
