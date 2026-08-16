# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T10:52:25.886645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.0324` n `230`; crypto_major avg `0.0421` n `8`; equity avg `-0.0164` n `114`; fx avg `0.0` n `6`; index avg `-0.0002` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.0237` n `791`
- 1h: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.0476` n `230`; crypto_major avg `-0.0334` n `8`; equity avg `-0.0429` n `114`; fx avg `-0.0003` n `6`; index avg `-0.0125` n `25`; metal avg `0.0071` n `20`; unknown avg `0.1092` n `791`
- 4h: commodity avg `0.0169` n `12`; crypto_alt avg `0.3714` n `230`; crypto_major avg `0.0786` n `8`; equity avg `-0.0361` n `114`; fx avg `0.002` n `6`; index avg `-0.0066` n `25`; metal avg `0.0045` n `20`; unknown avg `0.1265` n `791`
- 24h: commodity avg `0.1281` n `12`; crypto_alt avg `0.1029` n `230`; crypto_major avg `0.1303` n `8`; equity avg `0.3653` n `114`; fx avg `-0.036` n `6`; index avg `0.0484` n `25`; metal avg `0.0334` n `20`; unknown avg `0.1885` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2087`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
