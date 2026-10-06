# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T02:33:07.615634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.024` n `13`; crypto_alt avg `-0.1749` n `235`; crypto_major avg `-0.0665` n `8`; equity avg `-0.0981` n `149`; fx avg `0.0013` n `6`; index avg `-0.0173` n `26`; metal avg `-0.0117` n `20`; unknown avg `-0.1422` n `1074`
- 1h: commodity avg `0.05` n `13`; crypto_alt avg `-0.5076` n `235`; crypto_major avg `-0.2342` n `8`; equity avg `-0.0872` n `149`; fx avg `-0.0261` n `6`; index avg `-0.0326` n `26`; metal avg `-0.0664` n `20`; unknown avg `-0.2543` n `1072`
- 4h: commodity avg `0.084` n `13`; crypto_alt avg `-1.3224` n `235`; crypto_major avg `-0.5765` n `8`; equity avg `-0.2102` n `149`; fx avg `0.0033` n `6`; index avg `-0.0622` n `26`; metal avg `-0.1201` n `20`; unknown avg `0.3117` n `1066`
- 24h: commodity avg `-0.0006` n `13`; crypto_alt avg `-1.3566` n `235`; crypto_major avg `-0.6677` n `8`; equity avg `-0.1725` n `149`; fx avg `-0.0021` n `6`; index avg `0.0367` n `26`; metal avg `-0.0907` n `20`; unknown avg `630.8186` n `793`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1925`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
