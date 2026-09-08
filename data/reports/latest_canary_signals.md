# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T18:22:35.330745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1696` n `12`; crypto_alt avg `0.0354` n `233`; crypto_major avg `0.2188` n `8`; equity avg `0.0042` n `134`; fx avg `0.0201` n `6`; index avg `0.0064` n `26`; metal avg `-0.0002` n `20`; unknown avg `1.8066` n `797`
- 1h: commodity avg `0.2156` n `12`; crypto_alt avg `0.1126` n `233`; crypto_major avg `0.4479` n `8`; equity avg `-0.0073` n `134`; fx avg `-0.0034` n `6`; index avg `0.0163` n `26`; metal avg `-0.028` n `20`; unknown avg `-0.2969` n `795`
- 4h: commodity avg `-0.0508` n `12`; crypto_alt avg `0.6122` n `232`; crypto_major avg `1.0069` n `8`; equity avg `0.7045` n `134`; fx avg `0.0078` n `6`; index avg `0.0857` n `26`; metal avg `-0.0181` n `20`; unknown avg `-0.0319` n `765`
- 24h: commodity avg `-0.1259` n `12`; crypto_alt avg `0.8477` n `232`; crypto_major avg `0.6868` n `8`; equity avg `0.9802` n `134`; fx avg `-0.0616` n `6`; index avg `-0.0323` n `26`; metal avg `-0.0245` n `20`; unknown avg `8.7901` n `706`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
