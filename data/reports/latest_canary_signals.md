# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T08:22:28.197534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `-0.1298` n `230`; crypto_major avg `-0.1421` n `8`; equity avg `0.0294` n `114`; fx avg `0.0153` n `6`; index avg `-0.0` n `25`; metal avg `0.0178` n `20`; unknown avg `-0.0219` n `792`
- 1h: commodity avg `0.0983` n `12`; crypto_alt avg `-0.2244` n `230`; crypto_major avg `-0.3443` n `8`; equity avg `0.176` n `114`; fx avg `0.005` n `6`; index avg `0.0175` n `25`; metal avg `0.0174` n `20`; unknown avg `0.0113` n `792`
- 4h: commodity avg `-0.0606` n `12`; crypto_alt avg `-0.2061` n `230`; crypto_major avg `-0.1593` n `8`; equity avg `0.5304` n `114`; fx avg `0.0019` n `6`; index avg `0.0692` n `25`; metal avg `0.0459` n `20`; unknown avg `0.0042` n `776`
- 24h: commodity avg `-0.2051` n `12`; crypto_alt avg `-0.0665` n `230`; crypto_major avg `0.516` n `8`; equity avg `1.2322` n `114`; fx avg `-0.0199` n `6`; index avg `0.1428` n `25`; metal avg `0.2284` n `20`; unknown avg `0.1464` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
