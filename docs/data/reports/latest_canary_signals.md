# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T11:52:25.806185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.022` n `12`; crypto_alt avg `0.1238` n `228`; crypto_major avg `0.0541` n `8`; equity avg `-0.0156` n `88`; fx avg `0.0023` n `6`; index avg `0.0079` n `23`; metal avg `-0.0089` n `20`; unknown avg `0.1814` n `764`
- 1h: commodity avg `0.0628` n `12`; crypto_alt avg `0.2949` n `228`; crypto_major avg `0.3393` n `8`; equity avg `0.0395` n `88`; fx avg `0.0037` n `6`; index avg `0.0182` n `23`; metal avg `0.0003` n `20`; unknown avg `-0.1835` n `764`
- 4h: commodity avg `-0.0309` n `12`; crypto_alt avg `0.2658` n `228`; crypto_major avg `0.4056` n `8`; equity avg `0.0872` n `88`; fx avg `0.0125` n `6`; index avg `0.0492` n `23`; metal avg `0.0086` n `20`; unknown avg `-0.9596` n `750`
- 24h: commodity avg `0.1948` n `12`; crypto_alt avg `0.0335` n `228`; crypto_major avg `-0.5435` n `8`; equity avg `0.1112` n `88`; fx avg `-0.0009` n `6`; index avg `-0.0411` n `23`; metal avg `-0.0224` n `20`; unknown avg `15.6872` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2105`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1879`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
