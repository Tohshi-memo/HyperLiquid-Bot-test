# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T14:52:25.717379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `-1.7209` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0546` n `12`; crypto_alt avg `-0.1476` n `230`; crypto_major avg `-0.0359` n `8`; equity avg `0.4514` n `102`; fx avg `0.0118` n `6`; index avg `0.0481` n `25`; metal avg `0.0142` n `20`; unknown avg `-0.0635` n `785`
- 1h: commodity avg `0.2017` n `12`; crypto_alt avg `0.0998` n `230`; crypto_major avg `0.5794` n `8`; equity avg `2.3003` n `102`; fx avg `0.0113` n `6`; index avg `0.2707` n `25`; metal avg `0.1048` n `20`; unknown avg `-0.1308` n `785`
- 4h: commodity avg `0.086` n `12`; crypto_alt avg `0.8759` n `230`; crypto_major avg `1.1919` n `8`; equity avg `2.1674` n `102`; fx avg `-0.061` n `6`; index avg `0.1088` n `25`; metal avg `-0.2252` n `20`; unknown avg `0.3828` n `785`
- 24h: commodity avg `-0.2514` n `12`; crypto_alt avg `0.0457` n `230`; crypto_major avg `0.9418` n `8`; equity avg `1.6221` n `102`; fx avg `-0.1979` n `6`; index avg `-0.0134` n `25`; metal avg `-0.4689` n `20`; unknown avg `1.4999` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
