# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T23:31:38.177842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.0822` n `230`; crypto_major avg `0.0049` n `8`; equity avg `-0.0023` n `114`; fx avg `0.0016` n `6`; index avg `-0.0003` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0518` n `791`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `-0.4186` n `230`; crypto_major avg `-0.1824` n `8`; equity avg `-0.0058` n `114`; fx avg `0.0005` n `6`; index avg `0.0157` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.0776` n `791`
- 4h: commodity avg `-0.0256` n `12`; crypto_alt avg `-0.4914` n `230`; crypto_major avg `-0.2179` n `8`; equity avg `-0.0086` n `114`; fx avg `0.0008` n `6`; index avg `0.0028` n `25`; metal avg `-0.0037` n `20`; unknown avg `0.0351` n `791`
- 24h: commodity avg `-0.0916` n `12`; crypto_alt avg `0.1283` n `230`; crypto_major avg `0.0648` n `8`; equity avg `0.1442` n `114`; fx avg `0.0856` n `6`; index avg `0.006` n `25`; metal avg `-0.0126` n `20`; unknown avg `0.0642` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1838`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
