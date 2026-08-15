# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T22:37:26.514931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `-0.0579` n `230`; crypto_major avg `-0.0357` n `8`; equity avg `0.0166` n `114`; fx avg `-0.0018` n `6`; index avg `-0.0005` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0645` n `791`
- 1h: commodity avg `-0.019` n `12`; crypto_alt avg `-0.0829` n `230`; crypto_major avg `-0.0886` n `8`; equity avg `-0.0007` n `114`; fx avg `-0.0049` n `6`; index avg `0.0002` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.0244` n `791`
- 4h: commodity avg `-0.0148` n `12`; crypto_alt avg `-0.0416` n `230`; crypto_major avg `0.0602` n `8`; equity avg `0.0448` n `114`; fx avg `0.0003` n `6`; index avg `-0.0106` n `25`; metal avg `0.0012` n `20`; unknown avg `0.0569` n `791`
- 24h: commodity avg `-0.0834` n `12`; crypto_alt avg `0.7939` n `230`; crypto_major avg `0.5537` n `8`; equity avg `0.1607` n `114`; fx avg `0.0185` n `6`; index avg `-0.0105` n `25`; metal avg `0.0173` n `20`; unknown avg `0.0662` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1817`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
