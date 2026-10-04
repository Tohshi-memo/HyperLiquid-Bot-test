# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T15:07:31.645217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0683` n `13`; crypto_alt avg `0.0159` n `235`; crypto_major avg `0.0904` n `8`; equity avg `0.0159` n `144`; fx avg `0.0029` n `6`; index avg `-0.0027` n `26`; metal avg `0.0042` n `20`; unknown avg `0.3353` n `1076`
- 1h: commodity avg `0.132` n `13`; crypto_alt avg `0.3242` n `235`; crypto_major avg `0.143` n `8`; equity avg `0.0145` n `144`; fx avg `0.0015` n `6`; index avg `-0.0089` n `26`; metal avg `0.0077` n `20`; unknown avg `0.3852` n `1076`
- 4h: commodity avg `0.0016` n `13`; crypto_alt avg `0.2045` n `235`; crypto_major avg `0.0729` n `8`; equity avg `0.0549` n `144`; fx avg `0.0058` n `6`; index avg `-0.0125` n `26`; metal avg `0.0062` n `20`; unknown avg `0.0424` n `1070`
- 24h: commodity avg `0.0012` n `13`; crypto_alt avg `1.3182` n `235`; crypto_major avg `0.9984` n `8`; equity avg `0.2948` n `144`; fx avg `0.018` n `6`; index avg `0.0176` n `26`; metal avg `0.012` n `20`; unknown avg `0.0774` n `987`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2048`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
