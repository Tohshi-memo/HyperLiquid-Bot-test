# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T17:07:29.981585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0673` n `12`; crypto_alt avg `-0.175` n `234`; crypto_major avg `0.0688` n `8`; equity avg `0.0122` n `142`; fx avg `-0.0016` n `6`; index avg `0.0005` n `26`; metal avg `0.0044` n `20`; unknown avg `3.3749` n `967`
- 1h: commodity avg `-0.1362` n `12`; crypto_alt avg `-0.0114` n `234`; crypto_major avg `0.4497` n `8`; equity avg `0.0054` n `142`; fx avg `0.0054` n `6`; index avg `-0.0348` n `26`; metal avg `0.0213` n `20`; unknown avg `4.107` n `967`
- 4h: commodity avg `0.102` n `12`; crypto_alt avg `-0.8403` n `234`; crypto_major avg `-0.5924` n `8`; equity avg `-0.5598` n `142`; fx avg `0.032` n `6`; index avg `-0.0564` n `26`; metal avg `-0.2979` n `20`; unknown avg `12.031` n `875`
- 24h: commodity avg `0.0399` n `12`; crypto_alt avg `1.9247` n `234`; crypto_major avg `1.8527` n `8`; equity avg `0.1388` n `142`; fx avg `0.0805` n `6`; index avg `0.1821` n `26`; metal avg `0.062` n `20`; unknown avg `4.6219` n `820`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
