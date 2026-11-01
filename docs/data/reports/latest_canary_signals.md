# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T14:37:28.893751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `13`; crypto_alt avg `-0.0954` n `238`; crypto_major avg `-0.0351` n `8`; equity avg `-0.0013` n `156`; fx avg `-0.0009` n `6`; index avg `0.0104` n `27`; metal avg `-0.005` n `20`; unknown avg `0.8966` n `1263`
- 1h: commodity avg `0.0304` n `13`; crypto_alt avg `-0.0634` n `238`; crypto_major avg `0.1139` n `8`; equity avg `-0.0167` n `156`; fx avg `0.0011` n `6`; index avg `0.0227` n `27`; metal avg `-0.0086` n `20`; unknown avg `0.4086` n `1257`
- 4h: commodity avg `0.0135` n `13`; crypto_alt avg `0.1043` n `238`; crypto_major avg `-0.0637` n `8`; equity avg `-0.0523` n `156`; fx avg `-0.0035` n `6`; index avg `0.0374` n `27`; metal avg `-0.0104` n `20`; unknown avg `0.1614` n `1253`
- 24h: commodity avg `0.0545` n `13`; crypto_alt avg `0.5789` n `238`; crypto_major avg `0.5946` n `8`; equity avg `0.5184` n `156`; fx avg `-0.0198` n `6`; index avg `0.0726` n `27`; metal avg `0.0617` n `20`; unknown avg `1.656` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
