# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T23:37:30.787016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0493` n `13`; crypto_alt avg `0.3148` n `238`; crypto_major avg `0.3306` n `8`; equity avg `0.0362` n `156`; fx avg `0.0045` n `6`; index avg `-0.0039` n `27`; metal avg `0.0046` n `20`; unknown avg `127.8365` n `1262`
- 1h: commodity avg `0.0257` n `13`; crypto_alt avg `0.4366` n `238`; crypto_major avg `0.4205` n `8`; equity avg `0.1615` n `156`; fx avg `-0.006` n `6`; index avg `0.0111` n `27`; metal avg `-0.0012` n `20`; unknown avg `0.5446` n `1255`
- 4h: commodity avg `-0.1256` n `13`; crypto_alt avg `1.6683` n `238`; crypto_major avg `0.6982` n `8`; equity avg `0.8295` n `156`; fx avg `-0.044` n `6`; index avg `0.0845` n `27`; metal avg `0.081` n `20`; unknown avg `0.9414` n `1149`
- 24h: commodity avg `0.1052` n `13`; crypto_alt avg `2.2786` n `238`; crypto_major avg `-0.2443` n `8`; equity avg `-2.5478` n `156`; fx avg `-0.145` n `6`; index avg `-0.2318` n `27`; metal avg `-0.8978` n `20`; unknown avg `0.4157` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
