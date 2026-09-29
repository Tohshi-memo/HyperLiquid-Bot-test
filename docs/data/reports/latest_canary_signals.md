# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T13:52:34.033242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `0.2043` n `234`; crypto_major avg `0.1338` n `8`; equity avg `0.24` n `141`; fx avg `-0.0049` n `6`; index avg `0.0176` n `26`; metal avg `0.0429` n `20`; unknown avg `6.7712` n `963`
- 1h: commodity avg `-0.0942` n `12`; crypto_alt avg `0.29` n `234`; crypto_major avg `-0.0144` n `8`; equity avg `0.0223` n `141`; fx avg `0.0282` n `6`; index avg `-0.0234` n `26`; metal avg `0.0156` n `20`; unknown avg `116.961` n `961`
- 4h: commodity avg `-0.4097` n `12`; crypto_alt avg `0.8311` n `234`; crypto_major avg `0.5922` n `8`; equity avg `0.3875` n `141`; fx avg `-0.0179` n `6`; index avg `0.0447` n `26`; metal avg `0.0352` n `20`; unknown avg `3.6618` n `955`
- 24h: commodity avg `-0.7938` n `12`; crypto_alt avg `1.5402` n `234`; crypto_major avg `0.8449` n `8`; equity avg `0.3759` n `141`; fx avg `-0.1031` n `6`; index avg `-0.0024` n `26`; metal avg `-0.1843` n `20`; unknown avg `127.3541` n `810`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.18`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
