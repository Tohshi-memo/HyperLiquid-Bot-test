# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T08:22:27.051080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0459` n `12`; crypto_alt avg `0.039` n `230`; crypto_major avg `0.1198` n `8`; equity avg `-0.0357` n `98`; fx avg `0.0206` n `6`; index avg `0.0076` n `25`; metal avg `0.0325` n `20`; unknown avg `0.0299` n `773`
- 1h: commodity avg `0.0328` n `12`; crypto_alt avg `0.3133` n `230`; crypto_major avg `0.2917` n `8`; equity avg `-0.0971` n `98`; fx avg `-0.0011` n `6`; index avg `-0.019` n `25`; metal avg `-0.0427` n `20`; unknown avg `0.0861` n `772`
- 4h: commodity avg `0.2614` n `12`; crypto_alt avg `-0.5174` n `230`; crypto_major avg `-0.8727` n `8`; equity avg `-1.1709` n `98`; fx avg `-0.0488` n `6`; index avg `-0.2635` n `25`; metal avg `-0.1211` n `20`; unknown avg `-0.134` n `739`
- 24h: commodity avg `0.907` n `12`; crypto_alt avg `-0.8707` n `230`; crypto_major avg `-1.5327` n `8`; equity avg `0.4383` n `98`; fx avg `-0.0228` n `6`; index avg `-0.0031` n `25`; metal avg `0.3035` n `20`; unknown avg `0.0185` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1051`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0844`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0723`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0716`, n `666`, weak_sample_signal
