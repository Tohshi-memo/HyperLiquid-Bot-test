# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T07:37:27.512236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `-0.017` n `230`; crypto_major avg `-0.0398` n `8`; equity avg `0.0005` n `102`; fx avg `-0.0071` n `6`; index avg `-0.004` n `25`; metal avg `0.0064` n `20`; unknown avg `-0.0122` n `782`
- 1h: commodity avg `-0.0226` n `12`; crypto_alt avg `0.0826` n `230`; crypto_major avg `-0.0372` n `8`; equity avg `-0.0843` n `102`; fx avg `-0.0269` n `6`; index avg `0.0041` n `25`; metal avg `0.0206` n `20`; unknown avg `0.0096` n `782`
- 4h: commodity avg `0.0635` n `12`; crypto_alt avg `0.296` n `230`; crypto_major avg `0.0172` n `8`; equity avg `0.0322` n `102`; fx avg `-0.0664` n `6`; index avg `0.0297` n `25`; metal avg `0.0511` n `20`; unknown avg `0.3835` n `766`
- 24h: commodity avg `-1.1012` n `12`; crypto_alt avg `0.5044` n `230`; crypto_major avg `0.5619` n `8`; equity avg `0.8543` n `102`; fx avg `-0.1576` n `6`; index avg `0.2548` n `25`; metal avg `0.2283` n `20`; unknown avg `0.3462` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
