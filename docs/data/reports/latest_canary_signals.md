# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T13:37:27.312551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `0.0218` n `230`; crypto_major avg `0.0362` n `8`; equity avg `-0.0121` n `114`; fx avg `-0.0032` n `6`; index avg `-0.0006` n `25`; metal avg `0.0057` n `20`; unknown avg `-0.0019` n `791`
- 1h: commodity avg `-0.0298` n `12`; crypto_alt avg `0.1671` n `230`; crypto_major avg `0.194` n `8`; equity avg `0.0052` n `114`; fx avg `-0.0056` n `6`; index avg `-0.0` n `25`; metal avg `-0.0035` n `20`; unknown avg `-0.019` n `791`
- 4h: commodity avg `0.0307` n `12`; crypto_alt avg `0.0249` n `230`; crypto_major avg `0.1615` n `8`; equity avg `0.0305` n `114`; fx avg `-0.0126` n `6`; index avg `0.0167` n `25`; metal avg `-0.0099` n `20`; unknown avg `-0.0734` n `791`
- 24h: commodity avg `0.1646` n `12`; crypto_alt avg `1.095` n `230`; crypto_major avg `0.5379` n `8`; equity avg `-0.0168` n `114`; fx avg `0.1181` n `6`; index avg `-0.0489` n `25`; metal avg `0.0156` n `20`; unknown avg `-0.0867` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.186`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
