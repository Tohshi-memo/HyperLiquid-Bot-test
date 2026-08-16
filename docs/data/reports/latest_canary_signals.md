# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T07:22:25.256743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `12`; crypto_alt avg `0.1456` n `230`; crypto_major avg `0.037` n `8`; equity avg `-0.0343` n `114`; fx avg `0.0082` n `6`; index avg `0.0013` n `25`; metal avg `-0.0059` n `20`; unknown avg `0.0024` n `791`
- 1h: commodity avg `-0.0303` n `12`; crypto_alt avg `0.2706` n `230`; crypto_major avg `0.1656` n `8`; equity avg `0.0106` n `114`; fx avg `0.0058` n `6`; index avg `0.0119` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0024` n `791`
- 4h: commodity avg `-0.0657` n `12`; crypto_alt avg `0.0451` n `230`; crypto_major avg `-0.078` n `8`; equity avg `0.1455` n `114`; fx avg `0.0067` n `6`; index avg `0.0292` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.0273` n `759`
- 24h: commodity avg `0.1581` n `12`; crypto_alt avg `-0.0975` n `230`; crypto_major avg `0.027` n `8`; equity avg `0.3613` n `114`; fx avg `-0.0032` n `6`; index avg `0.0418` n `25`; metal avg `0.0244` n `20`; unknown avg `0.0431` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
