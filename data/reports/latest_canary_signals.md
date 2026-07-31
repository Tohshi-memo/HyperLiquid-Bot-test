# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T13:07:31.512689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0617` n `12`; crypto_alt avg `0.1862` n `230`; crypto_major avg `0.1672` n `8`; equity avg `0.0927` n `102`; fx avg `-0.0043` n `6`; index avg `0.0152` n `25`; metal avg `-0.0557` n `20`; unknown avg `0.6733` n `780`
- 1h: commodity avg `-0.0687` n `12`; crypto_alt avg `0.4355` n `230`; crypto_major avg `0.2975` n `8`; equity avg `-0.1971` n `102`; fx avg `0.0076` n `6`; index avg `-0.0329` n `25`; metal avg `-0.0856` n `20`; unknown avg `0.3502` n `780`
- 4h: commodity avg `0.4593` n `12`; crypto_alt avg `0.021` n `230`; crypto_major avg `0.0596` n `8`; equity avg `-0.6364` n `102`; fx avg `0.183` n `6`; index avg `-0.0959` n `25`; metal avg `-0.1337` n `20`; unknown avg `1.1505` n `780`
- 24h: commodity avg `0.6122` n `12`; crypto_alt avg `-0.2191` n `230`; crypto_major avg `-0.1015` n `8`; equity avg `5.1271` n `102`; fx avg `-0.0513` n `6`; index avg `0.7355` n `25`; metal avg `-0.0474` n `20`; unknown avg `1.2703` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
