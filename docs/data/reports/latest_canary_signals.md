# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T00:52:27.118161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.0557` n `230`; crypto_major avg `-0.0046` n `8`; equity avg `-0.0289` n `114`; fx avg `-0.0012` n `6`; index avg `-0.0031` n `25`; metal avg `0.0031` n `20`; unknown avg `-0.0367` n `791`
- 1h: commodity avg `-0.0095` n `12`; crypto_alt avg `0.0276` n `230`; crypto_major avg `-0.0145` n `8`; equity avg `-0.0232` n `114`; fx avg `-0.0009` n `6`; index avg `-0.0035` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0799` n `791`
- 4h: commodity avg `-0.0213` n `12`; crypto_alt avg `-0.3322` n `230`; crypto_major avg `-0.2208` n `8`; equity avg `-0.0217` n `114`; fx avg `-0.0` n `6`; index avg `0.0199` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.0215` n `791`
- 24h: commodity avg `-0.1165` n `12`; crypto_alt avg `0.0833` n `230`; crypto_major avg `0.055` n `8`; equity avg `0.1573` n `114`; fx avg `0.0274` n `6`; index avg `0.01` n `25`; metal avg `-0.0516` n `20`; unknown avg `-0.0036` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2238`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
