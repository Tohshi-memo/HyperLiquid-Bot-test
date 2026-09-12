# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T01:37:26.341884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.99` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0804` n `12`; crypto_alt avg `-0.0791` n `233`; crypto_major avg `-0.0519` n `8`; equity avg `0.0095` n `136`; fx avg `0.0038` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0033` n `20`; unknown avg `0.1749` n `834`
- 1h: commodity avg `-0.0673` n `12`; crypto_alt avg `0.1768` n `233`; crypto_major avg `0.0392` n `8`; equity avg `0.0208` n `136`; fx avg `0.0128` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0188` n `20`; unknown avg `0.4861` n `832`
- 4h: commodity avg `-0.1048` n `12`; crypto_alt avg `0.2307` n `233`; crypto_major avg `-0.4604` n `8`; equity avg `0.1062` n `136`; fx avg `0.002` n `6`; index avg `0.0328` n `26`; metal avg `-0.0425` n `20`; unknown avg `4.5371` n `812`
- 24h: commodity avg `-0.6135` n `12`; crypto_alt avg `1.2855` n `233`; crypto_major avg `1.443` n `8`; equity avg `0.8175` n `136`; fx avg `-0.1741` n `6`; index avg `0.3199` n `26`; metal avg `0.205` n `20`; unknown avg `13.9746` n `700`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
