# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T11:52:36.540649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0733` n `12`; crypto_alt avg `0.0087` n `230`; crypto_major avg `-0.0537` n `8`; equity avg `0.009` n `102`; fx avg `-0.0003` n `6`; index avg `0.0255` n `25`; metal avg `-0.0036` n `20`; unknown avg `-0.0121` n `782`
- 1h: commodity avg `0.0624` n `12`; crypto_alt avg `-0.0692` n `230`; crypto_major avg `-0.161` n `8`; equity avg `-0.2703` n `102`; fx avg `0.0111` n `6`; index avg `-0.0381` n `25`; metal avg `-0.0106` n `20`; unknown avg `-0.0471` n `782`
- 4h: commodity avg `0.2366` n `12`; crypto_alt avg `-0.3211` n `230`; crypto_major avg `-0.5494` n `8`; equity avg `-0.1943` n `102`; fx avg `0.0015` n `6`; index avg `-0.0535` n `25`; metal avg `-0.0251` n `20`; unknown avg `-0.0574` n `782`
- 24h: commodity avg `-0.9554` n `12`; crypto_alt avg `0.2874` n `230`; crypto_major avg `0.1593` n `8`; equity avg `0.6494` n `102`; fx avg `-0.0775` n `6`; index avg `0.2079` n `25`; metal avg `0.2343` n `20`; unknown avg `0.2626` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
