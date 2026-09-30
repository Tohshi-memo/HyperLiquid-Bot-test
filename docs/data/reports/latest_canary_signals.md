# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T15:22:35.211271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.18` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.073` n `12`; crypto_alt avg `-0.128` n `234`; crypto_major avg `0.0503` n `8`; equity avg `-0.0986` n `142`; fx avg `0.0122` n `6`; index avg `-0.0169` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.1499` n `961`
- 1h: commodity avg `0.1828` n `12`; crypto_alt avg `-0.2114` n `234`; crypto_major avg `-0.0716` n `8`; equity avg `-0.312` n `142`; fx avg `0.0616` n `6`; index avg `-0.0622` n `26`; metal avg `-0.1673` n `20`; unknown avg `0.447` n `909`
- 4h: commodity avg `0.2258` n `12`; crypto_alt avg `-0.2273` n `234`; crypto_major avg `-0.3912` n `8`; equity avg `0.1346` n `142`; fx avg `0.0046` n `6`; index avg `0.1378` n `26`; metal avg `-0.1435` n `20`; unknown avg `7.415` n `875`
- 24h: commodity avg `0.1554` n `12`; crypto_alt avg `-0.1727` n `234`; crypto_major avg `0.0107` n `8`; equity avg `-0.23` n `142`; fx avg `0.0567` n `6`; index avg `0.165` n `26`; metal avg `0.004` n `20`; unknown avg `13.1943` n `820`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
