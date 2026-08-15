# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T18:07:26.710311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.0546` n `230`; crypto_major avg `0.0287` n `8`; equity avg `0.0083` n `114`; fx avg `-0.0044` n `6`; index avg `-0.0068` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0348` n `791`
- 1h: commodity avg `0.0289` n `12`; crypto_alt avg `-0.0921` n `230`; crypto_major avg `-0.0346` n `8`; equity avg `0.0496` n `114`; fx avg `-0.001` n `6`; index avg `0.0009` n `25`; metal avg `0.0043` n `20`; unknown avg `0.0142` n `791`
- 4h: commodity avg `0.0236` n `12`; crypto_alt avg `0.3256` n `230`; crypto_major avg `0.2291` n `8`; equity avg `0.0358` n `114`; fx avg `-0.0075` n `6`; index avg `0.0043` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.043` n `791`
- 24h: commodity avg `-0.0824` n `12`; crypto_alt avg `0.8219` n `230`; crypto_major avg `0.6001` n `8`; equity avg `0.2577` n `114`; fx avg `0.0313` n `6`; index avg `0.0328` n `25`; metal avg `0.0367` n `20`; unknown avg `0.0068` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
