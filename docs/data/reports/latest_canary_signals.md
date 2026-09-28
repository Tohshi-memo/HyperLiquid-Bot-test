# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T08:22:30.458037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0489` n `12`; crypto_alt avg `0.2951` n `234`; crypto_major avg `0.1368` n `8`; equity avg `-0.2638` n `141`; fx avg `-0.0327` n `6`; index avg `-0.0044` n `26`; metal avg `-0.0429` n `20`; unknown avg `0.1996` n `962`
- 1h: commodity avg `0.0763` n `12`; crypto_alt avg `-0.0445` n `234`; crypto_major avg `0.0103` n `8`; equity avg `-0.2607` n `141`; fx avg `-0.0964` n `6`; index avg `-0.0062` n `26`; metal avg `0.0196` n `20`; unknown avg `11.3108` n `944`
- 4h: commodity avg `0.168` n `12`; crypto_alt avg `-1.7738` n `234`; crypto_major avg `-0.9588` n `8`; equity avg `-1.2` n `141`; fx avg `-0.0638` n `6`; index avg `-0.0973` n `26`; metal avg `-0.2653` n `20`; unknown avg `29.5529` n `920`
- 24h: commodity avg `-0.1957` n `12`; crypto_alt avg `-4.0162` n `234`; crypto_major avg `-3.1594` n `8`; equity avg `-2.6458` n `141`; fx avg `-0.0175` n `6`; index avg `-0.2548` n `26`; metal avg `-0.9452` n `20`; unknown avg `6.002` n `815`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
