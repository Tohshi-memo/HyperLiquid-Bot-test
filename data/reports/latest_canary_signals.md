# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T02:07:27.322854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0718` n `13`; crypto_alt avg `0.1298` n `238`; crypto_major avg `0.0541` n `8`; equity avg `0.0171` n `156`; fx avg `0.0011` n `6`; index avg `0.005` n `27`; metal avg `-0.0068` n `20`; unknown avg `1.3123` n `1256`
- 1h: commodity avg `0.0751` n `13`; crypto_alt avg `-0.109` n `238`; crypto_major avg `-0.0303` n `8`; equity avg `0.0453` n `156`; fx avg `-0.0055` n `6`; index avg `0.0056` n `27`; metal avg `0.0052` n `20`; unknown avg `0.1874` n `1254`
- 4h: commodity avg `0.0787` n `13`; crypto_alt avg `-0.2105` n `238`; crypto_major avg `-0.0563` n `8`; equity avg `0.0091` n `156`; fx avg `0.0058` n `6`; index avg `-0.0181` n `27`; metal avg `0.0047` n `20`; unknown avg `1.1673` n `1192`
- 24h: commodity avg `0.1136` n `13`; crypto_alt avg `-0.3505` n `238`; crypto_major avg `-0.1489` n `8`; equity avg `0.1013` n `156`; fx avg `-0.0001` n `6`; index avg `-0.0734` n `27`; metal avg `0.0559` n `20`; unknown avg `1.9379` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
