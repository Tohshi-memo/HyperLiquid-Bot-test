# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T04:56:05.173916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `12`; crypto_alt avg `-0.0014` n `230`; crypto_major avg `-0.0086` n `8`; equity avg `-0.0057` n `114`; fx avg `-0.0004` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0406` n `791`
- 1h: commodity avg `0.0153` n `12`; crypto_alt avg `0.1875` n `230`; crypto_major avg `-0.0005` n `8`; equity avg `0.0101` n `114`; fx avg `-0.006` n `6`; index avg `-0.0117` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.1015` n `791`
- 4h: commodity avg `-0.0086` n `12`; crypto_alt avg `0.0484` n `230`; crypto_major avg `0.2333` n `8`; equity avg `0.0759` n `114`; fx avg `0.0461` n `6`; index avg `-0.0082` n `25`; metal avg `-0.0488` n `20`; unknown avg `0.3159` n `791`
- 24h: commodity avg `0.179` n `12`; crypto_alt avg `0.4598` n `230`; crypto_major avg `-0.1949` n `8`; equity avg `-0.0701` n `114`; fx avg `0.1351` n `6`; index avg `-0.0392` n `25`; metal avg `0.4165` n `20`; unknown avg `0.0783` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
