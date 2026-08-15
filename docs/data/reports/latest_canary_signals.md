# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T21:07:28.032937+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `0.0162` n `230`; crypto_major avg `-0.0044` n `8`; equity avg `-0.0067` n `114`; fx avg `0.0011` n `6`; index avg `0.005` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.0694` n `791`
- 1h: commodity avg `-0.0401` n `12`; crypto_alt avg `-0.1226` n `230`; crypto_major avg `-0.0653` n `8`; equity avg `-0.0035` n `114`; fx avg `-0.0001` n `6`; index avg `-0.0111` n `25`; metal avg `-0.0057` n `20`; unknown avg `0.2106` n `791`
- 4h: commodity avg `0.041` n `12`; crypto_alt avg `-0.2038` n `230`; crypto_major avg `-0.079` n `8`; equity avg `0.0938` n `114`; fx avg `0.0004` n `6`; index avg `-0.0101` n `25`; metal avg `0.005` n `20`; unknown avg `1.0479` n `791`
- 24h: commodity avg `-0.0141` n `12`; crypto_alt avg `0.7967` n `230`; crypto_major avg `0.5704` n `8`; equity avg `0.1894` n `114`; fx avg `0.0072` n `6`; index avg `-0.0028` n `25`; metal avg `0.0322` n `20`; unknown avg `0.1536` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
