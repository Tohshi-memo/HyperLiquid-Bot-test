# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T13:54:22.983266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0306` n `12`; crypto_alt avg `0.0092` n `230`; crypto_major avg `0.004` n `8`; equity avg `0.0702` n `96`; fx avg `-0.0006` n `6`; index avg `-0.0054` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.0047` n `770`
- 1h: commodity avg `-0.0467` n `12`; crypto_alt avg `-0.2714` n `230`; crypto_major avg `-0.3114` n `8`; equity avg `0.0307` n `96`; fx avg `-0.0011` n `6`; index avg `0.0014` n `25`; metal avg `-0.0067` n `20`; unknown avg `-0.0535` n `770`
- 4h: commodity avg `0.072` n `12`; crypto_alt avg `-0.0961` n `230`; crypto_major avg `-0.0346` n `8`; equity avg `-0.0343` n `96`; fx avg `-0.0075` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0171` n `20`; unknown avg `-0.0933` n `769`
- 24h: commodity avg `0.3472` n `12`; crypto_alt avg `-0.2029` n `230`; crypto_major avg `0.6837` n `8`; equity avg `1.3681` n `96`; fx avg `0.0233` n `6`; index avg `0.2708` n `25`; metal avg `0.2944` n `20`; unknown avg `0.0431` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
