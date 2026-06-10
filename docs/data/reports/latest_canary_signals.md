# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T02:07:24.489561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `-0.096` n `228`; crypto_major avg `-0.1778` n `8`; equity avg `-0.1988` n `74`; fx avg `0.0044` n `6`; index avg `-0.0464` n `23`; metal avg `-0.2808` n `18`; unknown avg `-0.0982` n `547`
- 1h: commodity avg `0.1635` n `12`; crypto_alt avg `-0.1722` n `228`; crypto_major avg `-0.1205` n `8`; equity avg `-0.3288` n `74`; fx avg `0.0591` n `6`; index avg `-0.0613` n `23`; metal avg `0.02` n `18`; unknown avg `-0.3033` n `547`
- 4h: commodity avg `-0.0817` n `12`; crypto_alt avg `0.103` n `228`; crypto_major avg `-0.398` n `8`; equity avg `-0.3318` n `74`; fx avg `-0.0132` n `6`; index avg `-0.1633` n `23`; metal avg `-1.3319` n `18`; unknown avg `-0.357` n `547`
- 24h: commodity avg `-0.4945` n `12`; crypto_alt avg `-0.1213` n `228`; crypto_major avg `-2.2449` n `8`; equity avg `-2.3215` n `74`; fx avg `0.1341` n `6`; index avg `-0.9345` n `23`; metal avg `-2.7402` n `18`; unknown avg `-0.4019` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0475`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0349`, n `668`, weak_sample_signal
