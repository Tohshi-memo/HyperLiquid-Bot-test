# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T20:07:26.801753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `-0.2218` n `231`; crypto_major avg `-0.1041` n `8`; equity avg `0.0875` n `127`; fx avg `0.0083` n `6`; index avg `0.0315` n `26`; metal avg `-0.0142` n `20`; unknown avg `0.1058` n `792`
- 1h: commodity avg `-0.0481` n `12`; crypto_alt avg `-0.3289` n `231`; crypto_major avg `-0.4113` n `8`; equity avg `0.2899` n `127`; fx avg `0.0059` n `6`; index avg `0.0763` n `26`; metal avg `-0.0323` n `20`; unknown avg `0.0305` n `792`
- 4h: commodity avg `0.1856` n `12`; crypto_alt avg `-0.33` n `231`; crypto_major avg `0.1248` n `8`; equity avg `0.4147` n `127`; fx avg `0.0164` n `6`; index avg `0.0426` n `26`; metal avg `0.0832` n `20`; unknown avg `0.2818` n `792`
- 24h: commodity avg `0.3887` n `12`; crypto_alt avg `2.7828` n `231`; crypto_major avg `3.7958` n `8`; equity avg `1.5053` n `127`; fx avg `-0.0352` n `6`; index avg `0.1848` n `26`; metal avg `0.2344` n `20`; unknown avg `1.0802` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
