# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T22:32:45.091207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `-0.0434` n `230`; crypto_major avg `-0.0297` n `8`; equity avg `0.0122` n `112`; fx avg `0.0035` n `6`; index avg `0.0009` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.0163` n `782`
- 1h: commodity avg `-0.0789` n `12`; crypto_alt avg `-0.1454` n `230`; crypto_major avg `-0.0904` n `8`; equity avg `0.0361` n `112`; fx avg `0.0129` n `6`; index avg `0.0061` n `25`; metal avg `0.0211` n `20`; unknown avg `-0.0241` n `782`
- 4h: commodity avg `-0.3142` n `12`; crypto_alt avg `-0.2436` n `230`; crypto_major avg `0.1733` n `8`; equity avg `0.5086` n `112`; fx avg `0.0207` n `6`; index avg `0.0943` n `25`; metal avg `0.0687` n `20`; unknown avg `-0.1456` n `782`
- 24h: commodity avg `-0.2151` n `12`; crypto_alt avg `-0.4762` n `230`; crypto_major avg `-0.1865` n `8`; equity avg `1.7028` n `112`; fx avg `-0.1217` n `6`; index avg `0.0981` n `25`; metal avg `0.4786` n `20`; unknown avg `0.0815` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
