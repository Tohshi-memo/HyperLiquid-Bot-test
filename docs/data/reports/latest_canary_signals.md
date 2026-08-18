# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T08:06:55.525831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0432` n `12`; crypto_alt avg `-0.1082` n `230`; crypto_major avg `-0.2062` n `8`; equity avg `-0.5501` n `114`; fx avg `-0.0113` n `6`; index avg `-0.07` n `25`; metal avg `-0.0835` n `20`; unknown avg `-0.0268` n `795`
- 1h: commodity avg `0.0235` n `12`; crypto_alt avg `-0.1219` n `230`; crypto_major avg `-0.3893` n `8`; equity avg `-0.797` n `114`; fx avg `0.0078` n `6`; index avg `-0.128` n `25`; metal avg `-0.1528` n `20`; unknown avg `0.0104` n `794`
- 4h: commodity avg `-0.0022` n `12`; crypto_alt avg `0.2788` n `230`; crypto_major avg `0.0387` n `8`; equity avg `-0.8126` n `114`; fx avg `-0.004` n `6`; index avg `-0.1666` n `25`; metal avg `-0.0567` n `20`; unknown avg `0.0736` n `761`
- 24h: commodity avg `0.7085` n `12`; crypto_alt avg `-1.1681` n `230`; crypto_major avg `-0.1094` n `8`; equity avg `-2.3766` n `114`; fx avg `-0.0137` n `6`; index avg `-0.5239` n `25`; metal avg `-0.2902` n `20`; unknown avg `-0.0341` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
