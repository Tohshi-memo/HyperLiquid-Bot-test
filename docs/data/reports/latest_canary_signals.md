# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T21:04:05.206432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.61` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `0.0432` n `230`; crypto_major avg `0.0429` n `8`; equity avg `-0.0051` n `96`; fx avg `-0.0028` n `6`; index avg `-0.0028` n `25`; metal avg `-0.0018` n `20`; unknown avg `0.025` n `771`
- 1h: commodity avg `0.0242` n `12`; crypto_alt avg `0.0963` n `230`; crypto_major avg `0.1443` n `8`; equity avg `0.0403` n `96`; fx avg `0.0024` n `6`; index avg `0.0133` n `25`; metal avg `-0.0341` n `20`; unknown avg `0.0078` n `771`
- 4h: commodity avg `0.0214` n `12`; crypto_alt avg `0.2453` n `230`; crypto_major avg `0.1308` n `8`; equity avg `0.1353` n `96`; fx avg `0.0596` n `6`; index avg `0.054` n `25`; metal avg `0.01` n `20`; unknown avg `-0.0083` n `770`
- 24h: commodity avg `0.0025` n `12`; crypto_alt avg `0.0666` n `230`; crypto_major avg `0.3737` n `8`; equity avg `0.4348` n `96`; fx avg `0.1226` n `6`; index avg `-0.0148` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.0436` n `752`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1542`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1467`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1347`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.12`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.113`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.105`, n `666`, weak_sample_signal
