# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T19:52:27.677328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.033` n `12`; crypto_alt avg `-0.0292` n `230`; crypto_major avg `-0.1081` n `8`; equity avg `-0.0108` n `114`; fx avg `-0.0086` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.0805` n `791`
- 1h: commodity avg `-0.0243` n `12`; crypto_alt avg `0.0487` n `230`; crypto_major avg `0.0208` n `8`; equity avg `0.0116` n `114`; fx avg `-0.0117` n `6`; index avg `0.0111` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.1234` n `791`
- 4h: commodity avg `0.0394` n `12`; crypto_alt avg `-0.1885` n `230`; crypto_major avg `-0.0411` n `8`; equity avg `0.0388` n `114`; fx avg `-0.0084` n `6`; index avg `0.0167` n `25`; metal avg `0.0199` n `20`; unknown avg `-0.1181` n `791`
- 24h: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.3333` n `230`; crypto_major avg `-0.1087` n `8`; equity avg `0.2582` n `114`; fx avg `-0.0162` n `6`; index avg `0.0362` n `25`; metal avg `0.0473` n `20`; unknown avg `0.1542` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.216`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
