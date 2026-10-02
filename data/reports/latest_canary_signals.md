# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T00:07:26.900530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `0.0827` n `234`; crypto_major avg `0.0098` n `8`; equity avg `-0.0327` n `142`; fx avg `0.0298` n `6`; index avg `-0.0` n `26`; metal avg `-0.0493` n `20`; unknown avg `-0.0433` n `977`
- 1h: commodity avg `-0.0123` n `13`; crypto_alt avg `0.3894` n `234`; crypto_major avg `0.2275` n `8`; equity avg `-0.0386` n `142`; fx avg `0.0235` n `6`; index avg `-0.0191` n `26`; metal avg `0.0169` n `20`; unknown avg `0.004` n `977`
- 4h: commodity avg `-0.0595` n `13`; crypto_alt avg `-0.1577` n `234`; crypto_major avg `-0.1081` n `8`; equity avg `0.0733` n `142`; fx avg `0.0131` n `6`; index avg `-0.0023` n `26`; metal avg `0.0142` n `20`; unknown avg `-0.4724` n `893`
- 24h: commodity avg `0.0451` n `13`; crypto_alt avg `-0.4047` n `234`; crypto_major avg `-0.04` n `8`; equity avg `0.9063` n `142`; fx avg `-0.1445` n `6`; index avg `0.1397` n `26`; metal avg `0.0423` n `20`; unknown avg `-0.1201` n `816`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
