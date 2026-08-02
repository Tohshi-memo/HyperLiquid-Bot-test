# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T22:22:28.396954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.192` n `12`; crypto_alt avg `-0.0448` n `230`; crypto_major avg `-0.0327` n `8`; equity avg `-0.0118` n `102`; fx avg `0.0255` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0415` n `20`; unknown avg `-0.0085` n `783`
- 1h: commodity avg `-0.1823` n `12`; crypto_alt avg `0.182` n `230`; crypto_major avg `0.3253` n `8`; equity avg `0.0651` n `102`; fx avg `0.0079` n `6`; index avg `-0.0164` n `25`; metal avg `-0.1407` n `20`; unknown avg `1.4799` n `783`
- 4h: commodity avg `-0.0908` n `12`; crypto_alt avg `0.2872` n `230`; crypto_major avg `0.6258` n `8`; equity avg `0.2653` n `102`; fx avg `0.1542` n `6`; index avg `0.0255` n `25`; metal avg `-0.0568` n `20`; unknown avg `2.6935` n `782`
- 24h: commodity avg `-1.2805` n `12`; crypto_alt avg `1.4599` n `230`; crypto_major avg `2.1047` n `8`; equity avg `1.5304` n `102`; fx avg `-0.0028` n `6`; index avg `0.3276` n `25`; metal avg `0.2108` n `20`; unknown avg `1.6556` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
