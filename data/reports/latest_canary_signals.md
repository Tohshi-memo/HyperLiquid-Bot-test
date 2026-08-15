# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T22:34:03.687881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `-0.025` n `230`; crypto_major avg `0.0095` n `8`; equity avg `0.0201` n `114`; fx avg `-0.0018` n `6`; index avg `0.0002` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.0415` n `791`
- 1h: commodity avg `-0.0215` n `12`; crypto_alt avg `-0.0501` n `230`; crypto_major avg `-0.0435` n `8`; equity avg `0.0028` n `114`; fx avg `-0.0049` n `6`; index avg `0.0009` n `25`; metal avg `0.0005` n `20`; unknown avg `0.0186` n `791`
- 4h: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.0088` n `230`; crypto_major avg `0.1055` n `8`; equity avg `0.0484` n `114`; fx avg `0.0003` n `6`; index avg `-0.0099` n `25`; metal avg `0.002` n `20`; unknown avg `0.0661` n `791`
- 24h: commodity avg `-0.0859` n `12`; crypto_alt avg `0.8276` n `230`; crypto_major avg `0.5993` n `8`; equity avg `0.1643` n `114`; fx avg `0.0185` n `6`; index avg `-0.0098` n `25`; metal avg `0.0181` n `20`; unknown avg `0.0823` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
