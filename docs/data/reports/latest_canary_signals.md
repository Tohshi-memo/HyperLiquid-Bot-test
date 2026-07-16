# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T18:07:32.034848+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0403` n `12`; crypto_alt avg `0.1766` n `230`; crypto_major avg `0.2192` n `8`; equity avg `0.1457` n `94`; fx avg `-0.0072` n `6`; index avg `-0.0098` n `25`; metal avg `0.0112` n `20`; unknown avg `0.1016` n `768`
- 1h: commodity avg `0.0082` n `12`; crypto_alt avg `-0.2933` n `230`; crypto_major avg `-0.4287` n `8`; equity avg `-0.3353` n `94`; fx avg `0.0038` n `6`; index avg `-0.0802` n `25`; metal avg `-0.0822` n `20`; unknown avg `0.0017` n `768`
- 4h: commodity avg `-0.3886` n `12`; crypto_alt avg `-0.5036` n `230`; crypto_major avg `-1.1957` n `8`; equity avg `-1.4716` n `94`; fx avg `-0.0709` n `6`; index avg `-0.2064` n `25`; metal avg `-0.1871` n `20`; unknown avg `-0.2543` n `768`
- 24h: commodity avg `-0.248` n `12`; crypto_alt avg `-1.0638` n `230`; crypto_major avg `-2.3324` n `8`; equity avg `-3.8039` n `94`; fx avg `-0.1592` n `6`; index avg `-0.5297` n `25`; metal avg `-0.678` n `20`; unknown avg `-0.3053` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
