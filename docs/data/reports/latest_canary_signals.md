# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T14:52:27.371756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0689` n `13`; crypto_alt avg `0.0179` n `235`; crypto_major avg `0.103` n `8`; equity avg `0.0139` n `144`; fx avg `-0.0014` n `6`; index avg `-0.0013` n `26`; metal avg `0.0022` n `20`; unknown avg `0.0604` n `1078`
- 1h: commodity avg `-0.107` n `13`; crypto_alt avg `0.2274` n `235`; crypto_major avg `-0.0686` n `8`; equity avg `0.0021` n `144`; fx avg `-0.0036` n `6`; index avg `-0.0061` n `26`; metal avg `0.0058` n `20`; unknown avg `0.2323` n `1076`
- 4h: commodity avg `-0.0668` n `13`; crypto_alt avg `0.1947` n `235`; crypto_major avg `-0.0935` n `8`; equity avg `0.0396` n `144`; fx avg `0.0023` n `6`; index avg `-0.0073` n `26`; metal avg `0.0002` n `20`; unknown avg `0.2125` n `1070`
- 24h: commodity avg `-0.0612` n `13`; crypto_alt avg `1.0809` n `235`; crypto_major avg `0.7829` n `8`; equity avg `0.283` n `144`; fx avg `0.0132` n `6`; index avg `0.0219` n `26`; metal avg `0.007` n `20`; unknown avg `0.0048` n `963`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2052`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
