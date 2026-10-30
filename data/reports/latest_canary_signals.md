# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T03:52:27.742794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0394` n `13`; crypto_alt avg `0.371` n `238`; crypto_major avg `0.4202` n `8`; equity avg `0.1762` n `156`; fx avg `0.0062` n `6`; index avg `0.0167` n `27`; metal avg `-0.0221` n `20`; unknown avg `0.4734` n `1252`
- 1h: commodity avg `-0.051` n `13`; crypto_alt avg `1.2997` n `238`; crypto_major avg `1.4364` n `8`; equity avg `0.4656` n `156`; fx avg `-0.0419` n `6`; index avg `0.0479` n `27`; metal avg `-0.006` n `20`; unknown avg `2.5753` n `1242`
- 4h: commodity avg `0.1019` n `13`; crypto_alt avg `-0.2111` n `238`; crypto_major avg `1.153` n `8`; equity avg `0.0639` n `156`; fx avg `-0.039` n `6`; index avg `-0.1366` n `27`; metal avg `-0.2701` n `20`; unknown avg `0.8065` n `1226`
- 24h: commodity avg `-0.0771` n `13`; crypto_alt avg `-3.9691` n `238`; crypto_major avg `0.1989` n `8`; equity avg `-2.4568` n `155`; fx avg `0.1421` n `6`; index avg `-0.2627` n `27`; metal avg `-0.6559` n `20`; unknown avg `28.7967` n `974`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
