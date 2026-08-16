# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T07:07:29.209420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `-0.0055` n `230`; crypto_major avg `0.0262` n `8`; equity avg `0.0154` n `114`; fx avg `-0.0012` n `6`; index avg `0.0027` n `25`; metal avg `-0.002` n `20`; unknown avg `0.018` n `791`
- 1h: commodity avg `-0.0195` n `12`; crypto_alt avg `-0.0333` n `230`; crypto_major avg `0.0343` n `8`; equity avg `0.0534` n `114`; fx avg `-0.0011` n `6`; index avg `0.0104` n `25`; metal avg `0.004` n `20`; unknown avg `1.5572` n `791`
- 4h: commodity avg `-0.0364` n `12`; crypto_alt avg `-0.1112` n `230`; crypto_major avg `-0.1485` n `8`; equity avg `0.2101` n `114`; fx avg `-0.0053` n `6`; index avg `0.0241` n `25`; metal avg `0.0197` n `20`; unknown avg `0.0174` n `759`
- 24h: commodity avg `-0.0373` n `12`; crypto_alt avg `-0.2999` n `230`; crypto_major avg `-0.1267` n `8`; equity avg `0.4212` n `114`; fx avg `-0.017` n `6`; index avg `0.057` n `25`; metal avg `0.0281` n `20`; unknown avg `0.0643` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2112`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
