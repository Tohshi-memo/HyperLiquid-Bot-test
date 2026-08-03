# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T01:11:50.387580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0547` n `230`; crypto_major avg `-0.0619` n `8`; equity avg `0.1212` n `102`; fx avg `-0.0225` n `6`; index avg `0.0233` n `25`; metal avg `0.012` n `20`; unknown avg `-0.0342` n `784`
- 1h: commodity avg `0.0131` n `12`; crypto_alt avg `-0.2737` n `230`; crypto_major avg `-0.2625` n `8`; equity avg `0.5645` n `102`; fx avg `-0.2525` n `6`; index avg `-0.0109` n `25`; metal avg `-0.0825` n `20`; unknown avg `-0.0595` n `784`
- 4h: commodity avg `-0.0789` n `12`; crypto_alt avg `-0.5413` n `230`; crypto_major avg `-0.4533` n `8`; equity avg `0.4137` n `102`; fx avg `-0.2938` n `6`; index avg `-0.0715` n `25`; metal avg `-0.2111` n `20`; unknown avg `1.3985` n `783`
- 24h: commodity avg `-0.9691` n `12`; crypto_alt avg `0.2683` n `230`; crypto_major avg `0.8313` n `8`; equity avg `1.5795` n `102`; fx avg `-0.3173` n `6`; index avg `0.1848` n `25`; metal avg `0.0698` n `20`; unknown avg `1.505` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
