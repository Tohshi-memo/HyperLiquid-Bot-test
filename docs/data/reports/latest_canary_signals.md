# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T08:22:29.560818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0362` n `12`; crypto_alt avg `-0.1601` n `230`; crypto_major avg `-0.1027` n `8`; equity avg `0.1773` n `102`; fx avg `0.0071` n `6`; index avg `0.0396` n `25`; metal avg `-0.0358` n `20`; unknown avg `0.0404` n `774`
- 1h: commodity avg `-0.1037` n `12`; crypto_alt avg `-0.3177` n `230`; crypto_major avg `-0.2116` n `8`; equity avg `-0.0386` n `102`; fx avg `0.0054` n `6`; index avg `-0.0506` n `25`; metal avg `-0.0455` n `20`; unknown avg `-0.0024` n `774`
- 4h: commodity avg `-0.2838` n `12`; crypto_alt avg `-0.1622` n `230`; crypto_major avg `-0.2462` n `8`; equity avg `-0.1652` n `102`; fx avg `-0.0397` n `6`; index avg `-0.0147` n `25`; metal avg `0.0013` n `20`; unknown avg `-0.0188` n `758`
- 24h: commodity avg `-0.7014` n `12`; crypto_alt avg `-3.7668` n `230`; crypto_major avg `-3.6297` n `8`; equity avg `-3.9982` n `102`; fx avg `-0.1787` n `6`; index avg `-0.8358` n `25`; metal avg `-0.3879` n `20`; unknown avg `1158.569` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
