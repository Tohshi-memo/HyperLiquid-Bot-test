# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T14:37:26.953000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `13`; crypto_alt avg `0.1876` n `235`; crypto_major avg `0.035` n `8`; equity avg `-0.0043` n `144`; fx avg `0.0` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.1177` n `1078`
- 1h: commodity avg `-0.0549` n `13`; crypto_alt avg `0.2192` n `235`; crypto_major avg `-0.2117` n `8`; equity avg `-0.0036` n `144`; fx avg `-0.0004` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.1696` n `1076`
- 4h: commodity avg `0.0078` n `13`; crypto_alt avg `0.2897` n `235`; crypto_major avg `-0.1285` n `8`; equity avg `0.0356` n `144`; fx avg `0.006` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.2314` n `1070`
- 24h: commodity avg `0.0004` n `13`; crypto_alt avg `1.3516` n `235`; crypto_major avg `0.9591` n `8`; equity avg `0.2681` n `144`; fx avg `0.0146` n `6`; index avg `0.0217` n `26`; metal avg `0.0115` n `20`; unknown avg `0.0435` n `915`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2054`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
