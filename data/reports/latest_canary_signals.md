# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T23:07:26.393977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `-0.0731` n `230`; crypto_major avg `-0.0648` n `8`; equity avg `0.0184` n `114`; fx avg `-0.0019` n `6`; index avg `0.0046` n `25`; metal avg `-0.0004` n `20`; unknown avg `0.0705` n `791`
- 1h: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.2158` n `230`; crypto_major avg `-0.1254` n `8`; equity avg `0.0029` n `114`; fx avg `-0.002` n `6`; index avg `0.0078` n `25`; metal avg `-0.0052` n `20`; unknown avg `0.0679` n `791`
- 4h: commodity avg `-0.0349` n `12`; crypto_alt avg `-0.2214` n `230`; crypto_major avg `-0.0387` n `8`; equity avg `0.0354` n `114`; fx avg `0.0011` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.0405` n `791`
- 24h: commodity avg `-0.081` n `12`; crypto_alt avg `0.5677` n `230`; crypto_major avg `0.4009` n `8`; equity avg `0.1654` n `114`; fx avg `0.012` n `6`; index avg `0.0009` n `25`; metal avg `0.003` n `20`; unknown avg `0.1012` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1953`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
