# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T06:07:32.348457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0954` n `12`; crypto_alt avg `-0.027` n `230`; crypto_major avg `-0.053` n `8`; equity avg `0.0134` n `108`; fx avg `-0.0117` n `6`; index avg `0.0171` n `25`; metal avg `-0.0294` n `20`; unknown avg `0.0009` n `749`
- 1h: commodity avg `0.0331` n `12`; crypto_alt avg `0.0288` n `230`; crypto_major avg `0.0253` n `8`; equity avg `0.1405` n `108`; fx avg `-0.043` n `6`; index avg `0.0366` n `25`; metal avg `0.2221` n `20`; unknown avg `0.0637` n `749`
- 4h: commodity avg `-0.0319` n `12`; crypto_alt avg `0.2981` n `230`; crypto_major avg `0.0762` n `8`; equity avg `0.6044` n `108`; fx avg `0.0072` n `6`; index avg `0.0567` n `25`; metal avg `0.4946` n `20`; unknown avg `0.0834` n `749`
- 24h: commodity avg `-1.3735` n `12`; crypto_alt avg `0.4968` n `230`; crypto_major avg `0.8118` n `8`; equity avg `3.7866` n `108`; fx avg `-0.0204` n `6`; index avg `0.7754` n `25`; metal avg `1.1984` n `20`; unknown avg `0.4812` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
