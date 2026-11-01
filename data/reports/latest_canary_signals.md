# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T05:07:36.315599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `13`; crypto_alt avg `-0.0679` n `238`; crypto_major avg `-0.037` n `8`; equity avg `-0.018` n `156`; fx avg `0.0018` n `6`; index avg `-0.0029` n `27`; metal avg `-0.0005` n `20`; unknown avg `78.2406` n `1256`
- 1h: commodity avg `-0.0362` n `13`; crypto_alt avg `0.1771` n `238`; crypto_major avg `0.2156` n `8`; equity avg `0.1208` n `156`; fx avg `-0.0019` n `6`; index avg `0.0069` n `27`; metal avg `-0.002` n `20`; unknown avg `0.5582` n `1256`
- 4h: commodity avg `0.0529` n `13`; crypto_alt avg `0.0472` n `238`; crypto_major avg `-0.0653` n `8`; equity avg `0.1986` n `156`; fx avg `-0.009` n `6`; index avg `0.0281` n `27`; metal avg `0.0079` n `20`; unknown avg `1.488` n `1238`
- 24h: commodity avg `-0.0381` n `13`; crypto_alt avg `0.3539` n `238`; crypto_major avg `0.2344` n `8`; equity avg `0.2558` n `156`; fx avg `0.009` n `6`; index avg `-0.0078` n `27`; metal avg `0.0521` n `20`; unknown avg `2.9223` n `996`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
