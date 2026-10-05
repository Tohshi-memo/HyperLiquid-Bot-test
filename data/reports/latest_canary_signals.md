# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T08:22:39.243707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0495` n `13`; crypto_alt avg `-0.0786` n `235`; crypto_major avg `-0.0234` n `8`; equity avg `0.0432` n `144`; fx avg `0.0166` n `6`; index avg `0.0118` n `26`; metal avg `0.0385` n `20`; unknown avg `-0.1607` n `1061`
- 1h: commodity avg `-0.1328` n `13`; crypto_alt avg `0.2982` n `235`; crypto_major avg `0.3186` n `8`; equity avg `0.1698` n `144`; fx avg `0.0169` n `6`; index avg `0.0394` n `26`; metal avg `0.1783` n `20`; unknown avg `-0.4979` n `997`
- 4h: commodity avg `0.0275` n `13`; crypto_alt avg `1.0803` n `235`; crypto_major avg `1.0673` n `8`; equity avg `0.17` n `144`; fx avg `0.021` n `6`; index avg `0.0287` n `26`; metal avg `0.3295` n `20`; unknown avg `-0.4971` n `981`
- 24h: commodity avg `-0.3375` n `13`; crypto_alt avg `0.9846` n `235`; crypto_major avg `1.4998` n `8`; equity avg `0.4456` n `144`; fx avg `-0.0664` n `6`; index avg `-0.0003` n `26`; metal avg `0.3504` n `20`; unknown avg `-0.3398` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2021`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
