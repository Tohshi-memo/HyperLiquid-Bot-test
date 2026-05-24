# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T08:52:17.496535+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.0627` n `228`; crypto_major avg `-0.0419` n `8`; equity avg `0.0671` n `67`; fx avg `0.0021` n `6`; index avg `-0.0179` n `23`; metal avg `-0.0071` n `18`; unknown avg `0.0445` n `396`
- 1h: commodity avg `0.1192` n `12`; crypto_alt avg `0.1563` n `228`; crypto_major avg `0.331` n `8`; equity avg `0.0507` n `67`; fx avg `0.0069` n `6`; index avg `-0.0362` n `23`; metal avg `0.011` n `18`; unknown avg `1.1361` n `396`
- 4h: commodity avg `0.2423` n `12`; crypto_alt avg `-0.0267` n `228`; crypto_major avg `0.6727` n `8`; equity avg `0.0555` n `67`; fx avg `-0.0148` n `6`; index avg `0.0313` n `23`; metal avg `0.0886` n `18`; unknown avg `1.1978` n `386`
- 24h: commodity avg `-2.748` n `12`; crypto_alt avg `4.0206` n `228`; crypto_major avg `4.4261` n `8`; equity avg `2.6923` n `67`; fx avg `0.0798` n `6`; index avg `1.3714` n `23`; metal avg `1.2777` n `18`; unknown avg `2.1978` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
