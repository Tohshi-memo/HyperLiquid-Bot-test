# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T17:52:28.312566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `13`; crypto_alt avg `-0.1423` n `238`; crypto_major avg `-0.1577` n `8`; equity avg `-0.0453` n `156`; fx avg `0.0056` n `6`; index avg `-0.0034` n `27`; metal avg `-0.0017` n `20`; unknown avg `0.4766` n `1263`
- 1h: commodity avg `0.0221` n `13`; crypto_alt avg `-0.1373` n `238`; crypto_major avg `-0.0991` n `8`; equity avg `-0.0506` n `156`; fx avg `-0.0077` n `6`; index avg `-0.0018` n `27`; metal avg `0.0024` n `20`; unknown avg `158.6313` n `1257`
- 4h: commodity avg `-0.047` n `13`; crypto_alt avg `-0.5873` n `238`; crypto_major avg `-0.0802` n `8`; equity avg `-0.033` n `156`; fx avg `0.0297` n `6`; index avg `0.0287` n `27`; metal avg `0.0013` n `20`; unknown avg `-0.5396` n `1245`
- 24h: commodity avg `0.0461` n `13`; crypto_alt avg `-0.3769` n `238`; crypto_major avg `-0.0617` n `8`; equity avg `0.4056` n `156`; fx avg `0.0092` n `6`; index avg `0.0941` n `27`; metal avg `0.0566` n `20`; unknown avg `3.213` n `1012`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
