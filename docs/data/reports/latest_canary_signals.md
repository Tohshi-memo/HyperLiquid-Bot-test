# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T05:22:30.032599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `0.0275` n `230`; crypto_major avg `0.0962` n `8`; equity avg `0.1141` n `108`; fx avg `-0.0214` n `6`; index avg `0.0141` n `25`; metal avg `0.0203` n `20`; unknown avg `0.2783` n `781`
- 1h: commodity avg `0.0184` n `12`; crypto_alt avg `0.2396` n `230`; crypto_major avg `0.4851` n `8`; equity avg `0.4687` n `108`; fx avg `0.0504` n `6`; index avg `0.0707` n `25`; metal avg `-0.0239` n `20`; unknown avg `-0.0403` n `781`
- 4h: commodity avg `-0.1644` n `12`; crypto_alt avg `0.5525` n `230`; crypto_major avg `0.6357` n `8`; equity avg `1.1697` n `108`; fx avg `0.0066` n `6`; index avg `0.1072` n `25`; metal avg `0.4194` n `20`; unknown avg `-0.1337` n `781`
- 24h: commodity avg `-1.4639` n `12`; crypto_alt avg `0.5941` n `230`; crypto_major avg `0.8351` n `8`; equity avg `4.4635` n `108`; fx avg `0.0384` n `6`; index avg `0.8874` n `25`; metal avg `1.0497` n `20`; unknown avg `0.4593` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
