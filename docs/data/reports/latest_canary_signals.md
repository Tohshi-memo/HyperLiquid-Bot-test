# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T02:52:26.498878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0533` n `13`; crypto_alt avg `-0.0057` n `238`; crypto_major avg `0.0276` n `8`; equity avg `0.0067` n `156`; fx avg `0.0044` n `6`; index avg `-0.0001` n `27`; metal avg `0.0019` n `20`; unknown avg `1.1192` n `1262`
- 1h: commodity avg `0.0433` n `13`; crypto_alt avg `-0.2027` n `238`; crypto_major avg `-0.1792` n `8`; equity avg `-0.0374` n `156`; fx avg `0.0049` n `6`; index avg `-0.0003` n `27`; metal avg `-0.0047` n `20`; unknown avg `0.916` n `1254`
- 4h: commodity avg `0.0171` n `13`; crypto_alt avg `-0.1326` n `238`; crypto_major avg `0.1285` n `8`; equity avg `0.0346` n `156`; fx avg `-0.0015` n `6`; index avg `-0.0155` n `27`; metal avg `0.0054` n `20`; unknown avg `1.0725` n `1198`
- 24h: commodity avg `-0.0105` n `13`; crypto_alt avg `-0.7733` n `238`; crypto_major avg `-0.5249` n `8`; equity avg `0.0118` n `156`; fx avg `0.0224` n `6`; index avg `-0.0778` n `27`; metal avg `0.0535` n `20`; unknown avg `1.7836` n `1004`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
