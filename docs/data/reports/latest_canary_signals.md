# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T05:37:31.781041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `0.0392` n `230`; crypto_major avg `0.0172` n `8`; equity avg `0.0044` n `114`; fx avg `-0.0043` n `6`; index avg `0.0032` n `25`; metal avg `0.0169` n `20`; unknown avg `-0.013` n `791`
- 1h: commodity avg `-0.0511` n `12`; crypto_alt avg `0.0271` n `230`; crypto_major avg `-0.0527` n `8`; equity avg `0.0135` n `114`; fx avg `-0.0043` n `6`; index avg `0.0104` n `25`; metal avg `0.0147` n `20`; unknown avg `0.1064` n `791`
- 4h: commodity avg `-0.0161` n `12`; crypto_alt avg `-0.0338` n `230`; crypto_major avg `-0.0094` n `8`; equity avg `0.165` n `114`; fx avg `0.0019` n `6`; index avg `0.0181` n `25`; metal avg `0.0244` n `20`; unknown avg `-0.0177` n `791`
- 24h: commodity avg `-0.1075` n `12`; crypto_alt avg `-0.3721` n `230`; crypto_major avg `0.0243` n `8`; equity avg `0.3027` n `114`; fx avg `-0.017` n `6`; index avg `0.0417` n `25`; metal avg `0.0227` n `20`; unknown avg `0.0476` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.221`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
