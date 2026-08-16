# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T06:37:26.628343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `0.0188` n `230`; crypto_major avg `0.0625` n `8`; equity avg `0.0277` n `114`; fx avg `0.0042` n `6`; index avg `0.0055` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0023` n `791`
- 1h: commodity avg `-0.0059` n `12`; crypto_alt avg `-0.0751` n `230`; crypto_major avg `-0.0588` n `8`; equity avg `0.1055` n `114`; fx avg `0.0031` n `6`; index avg `0.0064` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.0124` n `759`
- 4h: commodity avg `-0.0542` n `12`; crypto_alt avg `-0.1023` n `230`; crypto_major avg `-0.2349` n `8`; equity avg `0.2243` n `114`; fx avg `0.0021` n `6`; index avg `0.0223` n `25`; metal avg `0.0301` n `20`; unknown avg `-0.0312` n `759`
- 24h: commodity avg `0.0019` n `12`; crypto_alt avg `-0.3506` n `230`; crypto_major avg `-0.1198` n `8`; equity avg `0.4507` n `114`; fx avg `-0.011` n `6`; index avg `0.0564` n `25`; metal avg `0.0447` n `20`; unknown avg `0.0473` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2139`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1692`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
