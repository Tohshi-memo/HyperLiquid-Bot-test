# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T13:22:52.683094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `13`; crypto_alt avg `-0.2287` n `235`; crypto_major avg `-0.1732` n `8`; equity avg `-0.0601` n `150`; fx avg `0.0008` n `6`; index avg `-0.0144` n `26`; metal avg `0.0298` n `20`; unknown avg `0.0626` n `1076`
- 1h: commodity avg `-0.0012` n `13`; crypto_alt avg `-0.4376` n `235`; crypto_major avg `-0.316` n `8`; equity avg `-0.0385` n `150`; fx avg `0.0125` n `6`; index avg `-0.0171` n `26`; metal avg `-0.1255` n `20`; unknown avg `113.4972` n `1074`
- 4h: commodity avg `0.1345` n `13`; crypto_alt avg `-1.32` n `235`; crypto_major avg `-1.0436` n `8`; equity avg `-0.5513` n `150`; fx avg `-0.0453` n `6`; index avg `-0.1417` n `26`; metal avg `-0.2151` n `20`; unknown avg `1.8515` n `1068`
- 24h: commodity avg `1.158` n `13`; crypto_alt avg `-5.6731` n `235`; crypto_major avg `-3.8537` n `8`; equity avg `-1.7493` n `150`; fx avg `-0.1624` n `6`; index avg `-0.398` n `26`; metal avg `-0.6487` n `20`; unknown avg `814.0777` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
