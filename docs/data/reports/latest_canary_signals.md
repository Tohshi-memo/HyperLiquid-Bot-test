# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T01:22:24.414949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0357` n `12`; crypto_alt avg `-0.2949` n `230`; crypto_major avg `-0.3195` n `8`; equity avg `-0.2705` n `94`; fx avg `-0.0068` n `6`; index avg `-0.0502` n `25`; metal avg `-0.062` n `20`; unknown avg `-0.0962` n `768`
- 1h: commodity avg `0.052` n `12`; crypto_alt avg `-0.4322` n `230`; crypto_major avg `-0.4477` n `8`; equity avg `-0.4104` n `94`; fx avg `0.0179` n `6`; index avg `-0.147` n `25`; metal avg `-0.2195` n `20`; unknown avg `-0.2653` n `768`
- 4h: commodity avg `-0.0512` n `12`; crypto_alt avg `-0.4799` n `230`; crypto_major avg `-0.6898` n `8`; equity avg `-0.6822` n `94`; fx avg `-0.0005` n `6`; index avg `-0.2004` n `25`; metal avg `-0.2081` n `20`; unknown avg `0.3746` n `766`
- 24h: commodity avg `0.0505` n `12`; crypto_alt avg `-0.2789` n `230`; crypto_major avg `0.094` n `8`; equity avg `-1.6873` n `93`; fx avg `0.1972` n `6`; index avg `-0.4283` n `25`; metal avg `-0.145` n `20`; unknown avg `0.0208` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
