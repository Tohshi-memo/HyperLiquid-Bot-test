# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T20:22:28.221262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `-0.0771` n `230`; crypto_major avg `-0.0391` n `8`; equity avg `0.0034` n `114`; fx avg `0.0` n `6`; index avg `-0.0065` n `25`; metal avg `-0.002` n `20`; unknown avg `0.2097` n `791`
- 1h: commodity avg `0.005` n `12`; crypto_alt avg `0.0098` n `230`; crypto_major avg `0.037` n `8`; equity avg `0.002` n `114`; fx avg `-0.001` n `6`; index avg `-0.0166` n `25`; metal avg `0.001` n `20`; unknown avg `-0.0318` n `791`
- 4h: commodity avg `0.0876` n `12`; crypto_alt avg `-0.1101` n `230`; crypto_major avg `0.0224` n `8`; equity avg `0.0758` n `114`; fx avg `-0.0012` n `6`; index avg `-0.0046` n `25`; metal avg `0.0063` n `20`; unknown avg `1.6265` n `791`
- 24h: commodity avg `0.0153` n `12`; crypto_alt avg `0.9215` n `230`; crypto_major avg `0.6051` n `8`; equity avg `0.2137` n `114`; fx avg `0.0027` n `6`; index avg `-0.007` n `25`; metal avg `0.0578` n `20`; unknown avg `0.1819` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2039`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
