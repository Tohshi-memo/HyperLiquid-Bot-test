# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T00:22:30.023531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0616` n `12`; crypto_alt avg `-0.3666` n `234`; crypto_major avg `-0.2493` n `8`; equity avg `-0.1254` n `141`; fx avg `0.0075` n `6`; index avg `-0.037` n `26`; metal avg `-0.0532` n `20`; unknown avg `-0.0141` n `963`
- 1h: commodity avg `-0.0296` n `12`; crypto_alt avg `-0.0581` n `234`; crypto_major avg `-0.1059` n `8`; equity avg `-0.0844` n `141`; fx avg `0.0136` n `6`; index avg `-0.0329` n `26`; metal avg `-0.0612` n `20`; unknown avg `-0.2617` n `955`
- 4h: commodity avg `0.0167` n `12`; crypto_alt avg `0.272` n `234`; crypto_major avg `-0.2604` n `8`; equity avg `0.0539` n `141`; fx avg `-0.0101` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0632` n `20`; unknown avg `-0.3526` n `929`
- 24h: commodity avg `0.0211` n `12`; crypto_alt avg `-4.009` n `234`; crypto_major avg `-2.5183` n `8`; equity avg `-3.1525` n `141`; fx avg `-0.0211` n `6`; index avg `-0.329` n `26`; metal avg `-0.9336` n `20`; unknown avg `86.0846` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
