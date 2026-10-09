# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T06:37:27.838961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0307` n `13`; crypto_alt avg `0.1074` n `235`; crypto_major avg `0.0907` n `8`; equity avg `0.0919` n `150`; fx avg `-0.0082` n `6`; index avg `0.0179` n `26`; metal avg `0.0035` n `20`; unknown avg `0.5759` n `1078`
- 1h: commodity avg `0.1086` n `13`; crypto_alt avg `0.0513` n `235`; crypto_major avg `-0.0687` n `8`; equity avg `0.1317` n `150`; fx avg `-0.0087` n `6`; index avg `0.0149` n `26`; metal avg `-0.079` n `20`; unknown avg `0.8741` n `1046`
- 4h: commodity avg `0.0303` n `13`; crypto_alt avg `1.473` n `235`; crypto_major avg `0.8188` n `8`; equity avg `0.6725` n `150`; fx avg `0.0177` n `6`; index avg `0.0807` n `26`; metal avg `0.1025` n `20`; unknown avg `1.7134` n `1040`
- 24h: commodity avg `-0.1352` n `13`; crypto_alt avg `-0.6684` n `235`; crypto_major avg `-1.6473` n `8`; equity avg `-0.689` n `150`; fx avg `0.1459` n `6`; index avg `-0.0037` n `26`; metal avg `0.4301` n `20`; unknown avg `6.7752` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
