# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T03:52:31.814053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `13`; crypto_alt avg `0.0458` n `238`; crypto_major avg `-0.0581` n `8`; equity avg `0.0024` n `156`; fx avg `0.0007` n `6`; index avg `-0.0052` n `27`; metal avg `0.0011` n `20`; unknown avg `0.6751` n `1260`
- 1h: commodity avg `0.0323` n `13`; crypto_alt avg `0.4832` n `238`; crypto_major avg `0.0722` n `8`; equity avg `0.1029` n `156`; fx avg `-0.0061` n `6`; index avg `0.0188` n `27`; metal avg `0.0033` n `20`; unknown avg `0.3971` n `1250`
- 4h: commodity avg `0.0622` n `13`; crypto_alt avg `0.2779` n `238`; crypto_major avg `0.0899` n `8`; equity avg `0.1235` n `156`; fx avg `0.0013` n `6`; index avg `-0.009` n `27`; metal avg `0.0105` n `20`; unknown avg `1.908` n `1196`
- 24h: commodity avg `-0.0294` n `13`; crypto_alt avg `-0.0944` n `238`; crypto_major avg `-0.0443` n `8`; equity avg `0.1016` n `156`; fx avg `-0.0005` n `6`; index avg `-0.0272` n `27`; metal avg `0.0602` n `20`; unknown avg `2.407` n `998`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
