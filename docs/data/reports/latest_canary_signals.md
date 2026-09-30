# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T01:52:25.661491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0271` n `12`; crypto_alt avg `0.1963` n `234`; crypto_major avg `0.2042` n `8`; equity avg `-0.0611` n `142`; fx avg `-0.0182` n `6`; index avg `0.0029` n `26`; metal avg `-0.0132` n `20`; unknown avg `0.3572` n `963`
- 1h: commodity avg `0.0522` n `12`; crypto_alt avg `0.9172` n `234`; crypto_major avg `0.3979` n `8`; equity avg `0.0103` n `142`; fx avg `-0.0639` n `6`; index avg `0.0023` n `26`; metal avg `-0.1099` n `20`; unknown avg `0.8252` n `961`
- 4h: commodity avg `0.1044` n `12`; crypto_alt avg `0.2895` n `234`; crypto_major avg `0.189` n `8`; equity avg `-0.0704` n `142`; fx avg `-0.0057` n `6`; index avg `0.0007` n `26`; metal avg `-0.1197` n `20`; unknown avg `0.4784` n `936`
- 24h: commodity avg `-0.9027` n `12`; crypto_alt avg `2.5125` n `234`; crypto_major avg `0.9379` n `8`; equity avg `0.8756` n `142`; fx avg `-0.1605` n `6`; index avg `0.1006` n `26`; metal avg `0.1546` n `20`; unknown avg `3100.1731` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
