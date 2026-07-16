# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T14:37:44.219135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2265` n `12`; crypto_alt avg `0.0459` n `230`; crypto_major avg `0.1461` n `8`; equity avg `0.1823` n `94`; fx avg `-0.0115` n `6`; index avg `0.0407` n `25`; metal avg `0.0726` n `20`; unknown avg `0.0244` n `768`
- 1h: commodity avg `-0.2022` n `12`; crypto_alt avg `0.1446` n `230`; crypto_major avg `0.2822` n `8`; equity avg `-0.289` n `94`; fx avg `-0.0028` n `6`; index avg `0.0507` n `25`; metal avg `0.0285` n `20`; unknown avg `0.0526` n `768`
- 4h: commodity avg `0.0146` n `12`; crypto_alt avg `0.5556` n `230`; crypto_major avg `0.4138` n `8`; equity avg `-0.9514` n `94`; fx avg `0.0261` n `6`; index avg `-0.0355` n `25`; metal avg `-0.2597` n `20`; unknown avg `0.213` n `768`
- 24h: commodity avg `0.092` n `12`; crypto_alt avg `-0.6304` n `230`; crypto_major avg `-1.3585` n `8`; equity avg `-2.3334` n `94`; fx avg `-0.0148` n `6`; index avg `-0.2049` n `25`; metal avg `-0.4326` n `20`; unknown avg `-0.0233` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
