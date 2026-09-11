# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T22:52:32.009577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `-0.0958` n `233`; crypto_major avg `-0.1337` n `8`; equity avg `-0.0135` n `136`; fx avg `0.0054` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0072` n `20`; unknown avg `0.1097` n `830`
- 1h: commodity avg `0.026` n `12`; crypto_alt avg `-0.3502` n `233`; crypto_major avg `-0.5259` n `8`; equity avg `-0.029` n `136`; fx avg `0.002` n `6`; index avg `0.0036` n `26`; metal avg `-0.0434` n `20`; unknown avg `6.1044` n `828`
- 4h: commodity avg `-0.1182` n `12`; crypto_alt avg `-0.2909` n `233`; crypto_major avg `-0.2359` n `8`; equity avg `-0.0529` n `136`; fx avg `-0.0098` n `6`; index avg `-0.0113` n `26`; metal avg `0.0082` n `20`; unknown avg `0.9994` n `770`
- 24h: commodity avg `-0.7441` n `12`; crypto_alt avg `-0.0062` n `233`; crypto_major avg `0.7606` n `8`; equity avg `0.8421` n `136`; fx avg `-0.1771` n `6`; index avg `0.3295` n `26`; metal avg `0.2833` n `20`; unknown avg `1.9476` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
