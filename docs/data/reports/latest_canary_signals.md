# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T12:22:27.089408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1164` n `12`; crypto_alt avg `0.0738` n `230`; crypto_major avg `0.0941` n `8`; equity avg `0.0575` n `102`; fx avg `0.0041` n `6`; index avg `0.0022` n `25`; metal avg `0.0015` n `20`; unknown avg `0.036` n `782`
- 1h: commodity avg `-0.05` n `12`; crypto_alt avg `0.0746` n `230`; crypto_major avg `-0.0601` n `8`; equity avg `-0.1466` n `102`; fx avg `-0.0033` n `6`; index avg `-0.0398` n `25`; metal avg `-0.0136` n `20`; unknown avg `-0.0095` n `782`
- 4h: commodity avg `0.1454` n `12`; crypto_alt avg `-0.2002` n `230`; crypto_major avg `-0.4765` n `8`; equity avg `-0.3432` n `102`; fx avg `0.0059` n `6`; index avg `-0.0855` n `25`; metal avg `-0.028` n `20`; unknown avg `-0.0182` n `782`
- 24h: commodity avg `-1.0784` n `12`; crypto_alt avg `0.1702` n `230`; crypto_major avg `0.09` n `8`; equity avg `0.7209` n `102`; fx avg `-0.0726` n `6`; index avg `0.2053` n `25`; metal avg `0.2302` n `20`; unknown avg `0.231` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
