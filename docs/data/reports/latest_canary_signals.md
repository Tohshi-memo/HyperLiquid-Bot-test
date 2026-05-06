# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T14:22:19.004364+00:00`
- Correlation status: `ready`
- Asset price records: `461`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `15.8` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.1584` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.5874` n `12`; crypto_alt avg `0.3537` n `228`; crypto_major avg `0.3682` n `8`; equity avg `0.1423` n `65`; fx avg `-0.0228` n `4`; index avg `-0.0432` n `23`; metal avg `0.2742` n `18`; unknown avg `2.1157` n `356`
- 1h: commodity avg `-0.5751` n `12`; crypto_alt avg `-1.0002` n `228`; crypto_major avg `-0.8576` n `8`; equity avg `-0.3294` n `65`; fx avg `-0.0395` n `4`; index avg `-0.0073` n `23`; metal avg `0.6206` n `18`; unknown avg `5.354` n `356`
- 4h: commodity avg `0.1749` n `7`; crypto_alt avg `-1.6312` n `223`; crypto_major avg `-1.4221` n `7`; equity avg `-1.1599` n `47`; fx avg `-0.0062` n `4`; index avg `-0.2637` n `6`; metal avg `0.0447` n `7`; unknown avg `7.5479` n `313`
- 24h: commodity avg `-2.6387` n `7`; crypto_alt avg `1.9273` n `223`; crypto_major avg `0.8744` n `7`; equity avg `1.3353` n `47`; fx avg `-0.6174` n `4`; index avg `1.9039` n `6`; metal avg `2.57` n `7`; unknown avg `18.4305` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1631`, n `457`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1573`, n `457`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1381`, n `457`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1239`, n `457`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `457`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `457`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0952`, n `453`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0862`, n `453`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0856`, n `457`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0856`, n `453`, weak_sample_signal
