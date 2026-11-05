# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T10:07:24.518562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0663` n `13`; crypto_alt avg `-0.1014` n `239`; crypto_major avg `-0.0285` n `8`; equity avg `-0.1653` n `158`; fx avg `0.0093` n `6`; index avg `-0.0187` n `27`; metal avg `-0.0062` n `20`; unknown avg `1.8938` n `1255`
- 1h: commodity avg `0.1407` n `13`; crypto_alt avg `-0.1044` n `239`; crypto_major avg `0.0314` n `8`; equity avg `0.305` n `158`; fx avg `-0.0389` n `6`; index avg `0.0354` n `27`; metal avg `-0.0396` n `20`; unknown avg `15.0281` n `1233`
- 4h: commodity avg `0.4012` n `13`; crypto_alt avg `0.5095` n `239`; crypto_major avg `0.3802` n `8`; equity avg `0.6646` n `158`; fx avg `-0.0604` n `6`; index avg `0.0891` n `27`; metal avg `0.0228` n `20`; unknown avg `16.4085` n `1153`
- 24h: commodity avg `-1.4574` n `13`; crypto_alt avg `0.7232` n `239`; crypto_major avg `1.7246` n `8`; equity avg `-3.1047` n `158`; fx avg `-0.05` n `6`; index avg `-0.2695` n `27`; metal avg `0.5562` n `20`; unknown avg `0.3673` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2465`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.187`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
