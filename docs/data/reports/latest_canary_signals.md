# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T09:45:20.051183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `0.0094` n `230`; crypto_major avg `0.0045` n `8`; equity avg `0.0039` n `114`; fx avg `0.0005` n `6`; index avg `-0.001` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0067` n `791`
- 1h: commodity avg `0.0247` n `12`; crypto_alt avg `-0.0021` n `230`; crypto_major avg `0.0361` n `8`; equity avg `-0.0145` n `114`; fx avg `0.0007` n `6`; index avg `-0.0038` n `25`; metal avg `0.0102` n `20`; unknown avg `0.0073` n `791`
- 4h: commodity avg `-0.1919` n `12`; crypto_alt avg `0.0145` n `230`; crypto_major avg `-0.1056` n `8`; equity avg `0.028` n `114`; fx avg `-0.003` n `6`; index avg `0.0073` n `25`; metal avg `0.0137` n `20`; unknown avg `-0.0419` n `765`
- 24h: commodity avg `-0.1229` n `12`; crypto_alt avg `1.1615` n `230`; crypto_major avg `0.0716` n `8`; equity avg `-0.4448` n `114`; fx avg `0.1709` n `6`; index avg `-0.1204` n `25`; metal avg `0.1811` n `20`; unknown avg `-0.0682` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
