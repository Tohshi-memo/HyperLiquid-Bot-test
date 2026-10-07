# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T07:07:34.015476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0468` n `13`; crypto_alt avg `0.0842` n `235`; crypto_major avg `-0.0711` n `8`; equity avg `0.0689` n `150`; fx avg `0.0103` n `6`; index avg `0.0154` n `26`; metal avg `0.0214` n `20`; unknown avg `0.3761` n `1074`
- 1h: commodity avg `-0.0157` n `13`; crypto_alt avg `0.3224` n `235`; crypto_major avg `0.0826` n `8`; equity avg `0.0569` n `150`; fx avg `0.0119` n `6`; index avg `-0.0017` n `26`; metal avg `-0.045` n `20`; unknown avg `0.2922` n `1074`
- 4h: commodity avg `0.1059` n `13`; crypto_alt avg `0.0523` n `235`; crypto_major avg `0.258` n `8`; equity avg `0.0441` n `150`; fx avg `-0.0223` n `6`; index avg `-0.0378` n `26`; metal avg `-0.1346` n `20`; unknown avg `0.1028` n `1046`
- 24h: commodity avg `0.8153` n `13`; crypto_alt avg `-2.7206` n `235`; crypto_major avg `-1.7526` n `8`; equity avg `-0.0526` n `149`; fx avg `0.0536` n `6`; index avg `-0.0559` n `26`; metal avg `-0.1294` n `20`; unknown avg `820.9787` n `970`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
