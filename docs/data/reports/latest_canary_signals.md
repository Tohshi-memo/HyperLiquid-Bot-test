# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T04:52:25.439087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0224` n `12`; crypto_alt avg `0.2972` n `230`; crypto_major avg `0.2785` n `8`; equity avg `0.23` n `96`; fx avg `-0.0063` n `6`; index avg `0.0338` n `25`; metal avg `0.0019` n `20`; unknown avg `0.1764` n `768`
- 1h: commodity avg `0.0235` n `12`; crypto_alt avg `0.0548` n `230`; crypto_major avg `-0.0334` n `8`; equity avg `-0.255` n `96`; fx avg `-0.0142` n `6`; index avg `-0.0983` n `25`; metal avg `-0.0978` n `20`; unknown avg `-0.0953` n `768`
- 4h: commodity avg `-0.0722` n `12`; crypto_alt avg `-0.1435` n `230`; crypto_major avg `-0.4378` n `8`; equity avg `-1.1829` n `94`; fx avg `0.0068` n `6`; index avg `-0.2687` n `25`; metal avg `-0.1847` n `20`; unknown avg `0.1683` n `768`
- 24h: commodity avg `-0.0474` n `12`; crypto_alt avg `-1.7181` n `230`; crypto_major avg `-2.7689` n `8`; equity avg `-5.379` n `94`; fx avg `-0.133` n `6`; index avg `-0.756` n `25`; metal avg `-0.8719` n `20`; unknown avg `-0.4797` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
