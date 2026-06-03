# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T17:52:28.173096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1263` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0565` n `12`; crypto_alt avg `-0.2626` n `228`; crypto_major avg `-0.2592` n `8`; equity avg `0.1313` n `73`; fx avg `0.0281` n `6`; index avg `0.0708` n `23`; metal avg `-0.0201` n `18`; unknown avg `-0.0832` n `419`
- 1h: commodity avg `0.062` n `12`; crypto_alt avg `0.4342` n `228`; crypto_major avg `0.3894` n `8`; equity avg `0.3648` n `73`; fx avg `-0.0031` n `6`; index avg `0.1192` n `23`; metal avg `0.0203` n `18`; unknown avg `0.0809` n `419`
- 4h: commodity avg `0.4688` n `12`; crypto_alt avg `-0.873` n `228`; crypto_major avg `-0.9573` n `8`; equity avg `-0.3702` n `73`; fx avg `0.0094` n `6`; index avg `0.169` n `23`; metal avg `-0.4722` n `18`; unknown avg `-0.0239` n `419`
- 24h: commodity avg `0.8198` n `12`; crypto_alt avg `0.2232` n `228`; crypto_major avg `-2.5914` n `8`; equity avg `-1.7467` n `72`; fx avg `0.0422` n `6`; index avg `-0.0918` n `23`; metal avg `-1.8271` n `18`; unknown avg `0.4671` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
