# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T12:07:30.462449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.079` n `12`; crypto_alt avg `-0.0712` n `230`; crypto_major avg `-0.1323` n `8`; equity avg `-0.1829` n `92`; fx avg `-0.0008` n `6`; index avg `-0.055` n `25`; metal avg `-0.0596` n `20`; unknown avg `0.005` n `766`
- 1h: commodity avg `0.1267` n `12`; crypto_alt avg `-0.1908` n `230`; crypto_major avg `-0.2423` n `8`; equity avg `-0.2628` n `92`; fx avg `-0.0135` n `6`; index avg `-0.0695` n `25`; metal avg `-0.0676` n `20`; unknown avg `-0.0205` n `766`
- 4h: commodity avg `0.1457` n `12`; crypto_alt avg `-0.1104` n `230`; crypto_major avg `-0.2938` n `8`; equity avg `0.1998` n `92`; fx avg `-0.0347` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0822` n `20`; unknown avg `-0.1371` n `766`
- 24h: commodity avg `-0.0312` n `12`; crypto_alt avg `-1.1852` n `230`; crypto_major avg `-1.427` n `8`; equity avg `-2.1287` n `92`; fx avg `-0.0562` n `6`; index avg `-0.4693` n `25`; metal avg `-0.2719` n `20`; unknown avg `-0.1038` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
