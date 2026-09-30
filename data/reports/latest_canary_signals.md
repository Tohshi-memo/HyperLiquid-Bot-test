# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T02:07:29.613187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0572` n `12`; crypto_alt avg `0.0962` n `234`; crypto_major avg `0.1781` n `8`; equity avg `0.1138` n `142`; fx avg `-0.0185` n `6`; index avg `0.0065` n `26`; metal avg `0.0314` n `20`; unknown avg `4.4619` n `961`
- 1h: commodity avg `-0.0283` n `12`; crypto_alt avg `0.496` n `234`; crypto_major avg `0.3814` n `8`; equity avg `0.0587` n `142`; fx avg `-0.0678` n `6`; index avg `0.0003` n `26`; metal avg `-0.045` n `20`; unknown avg `5.0462` n `961`
- 4h: commodity avg `0.1593` n `12`; crypto_alt avg `0.4166` n `234`; crypto_major avg `0.2822` n `8`; equity avg `-0.023` n `142`; fx avg `-0.0228` n `6`; index avg `-0.024` n `26`; metal avg `-0.1194` n `20`; unknown avg `6.1474` n `954`
- 24h: commodity avg `-0.9281` n `12`; crypto_alt avg `2.8041` n `234`; crypto_major avg `1.095` n `8`; equity avg `1.1872` n `142`; fx avg `-0.1771` n `6`; index avg `0.1303` n `26`; metal avg `0.2124` n `20`; unknown avg `3101.7959` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1793`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
