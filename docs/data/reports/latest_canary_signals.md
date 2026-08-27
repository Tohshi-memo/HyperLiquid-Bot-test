# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T18:37:30.621660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `0.0929` n `231`; crypto_major avg `0.2694` n `8`; equity avg `-0.0035` n `127`; fx avg `-0.0007` n `6`; index avg `-0.0249` n `26`; metal avg `-0.0172` n `20`; unknown avg `0.0638` n `792`
- 1h: commodity avg `0.0914` n `12`; crypto_alt avg `-0.9159` n `231`; crypto_major avg `-0.5717` n `8`; equity avg `-0.2145` n `127`; fx avg `0.0095` n `6`; index avg `-0.0988` n `26`; metal avg `-0.0493` n `20`; unknown avg `0.3466` n `792`
- 4h: commodity avg `0.13` n `12`; crypto_alt avg `-0.3958` n `231`; crypto_major avg `-0.0505` n `8`; equity avg `-0.3003` n `127`; fx avg `0.0002` n `6`; index avg `-0.0586` n `26`; metal avg `0.1937` n `20`; unknown avg `0.2782` n `792`
- 24h: commodity avg `0.4229` n `12`; crypto_alt avg `2.8281` n `231`; crypto_major avg `3.7513` n `8`; equity avg `1.3811` n `127`; fx avg `-0.0462` n `6`; index avg `0.1111` n `26`; metal avg `0.1605` n `20`; unknown avg `1.0106` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
