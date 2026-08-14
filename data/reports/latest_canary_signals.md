# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T14:52:43.754346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0342` n `12`; crypto_alt avg `-0.0621` n `230`; crypto_major avg `-0.0984` n `8`; equity avg `-0.1303` n `114`; fx avg `0.0117` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0235` n `20`; unknown avg `-0.0544` n `787`
- 1h: commodity avg `0.1685` n `12`; crypto_alt avg `-0.1817` n `230`; crypto_major avg `-0.1176` n `8`; equity avg `-0.2828` n `114`; fx avg `0.0066` n `6`; index avg `-0.0512` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.1444` n `786`
- 4h: commodity avg `0.1772` n `12`; crypto_alt avg `-0.1061` n `230`; crypto_major avg `-0.3988` n `8`; equity avg `-0.2369` n `114`; fx avg `0.0468` n `6`; index avg `-0.0597` n `25`; metal avg `0.2046` n `20`; unknown avg `3.1295` n `786`
- 24h: commodity avg `0.2023` n `12`; crypto_alt avg `-1.2017` n `230`; crypto_major avg `-1.4959` n `8`; equity avg `-0.21` n `114`; fx avg `0.0264` n `6`; index avg `-0.0099` n `25`; metal avg `0.0512` n `20`; unknown avg `0.289` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2022`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
