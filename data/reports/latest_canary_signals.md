# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T04:22:29.359686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0329` n `12`; crypto_alt avg `0.1797` n `234`; crypto_major avg `0.1273` n `8`; equity avg `0.0543` n `137`; fx avg `-0.0171` n `6`; index avg `0.0023` n `27`; metal avg `0.0088` n `20`; unknown avg `1.1364` n `919`
- 1h: commodity avg `0.0084` n `12`; crypto_alt avg `0.1901` n `234`; crypto_major avg `0.0411` n `8`; equity avg `0.152` n `137`; fx avg `-0.0293` n `6`; index avg `0.0041` n `27`; metal avg `-0.0302` n `20`; unknown avg `0.6667` n `917`
- 4h: commodity avg `-0.0826` n `12`; crypto_alt avg `0.1054` n `234`; crypto_major avg `0.4551` n `8`; equity avg `0.6919` n `137`; fx avg `0.0164` n `6`; index avg `0.0919` n `27`; metal avg `0.3061` n `20`; unknown avg `0.4136` n `907`
- 24h: commodity avg `0.1438` n `12`; crypto_alt avg `-3.058` n `234`; crypto_major avg `-3.0375` n `8`; equity avg `-0.386` n `137`; fx avg `0.1939` n `6`; index avg `0.0317` n `27`; metal avg `0.3859` n `20`; unknown avg `18796.1312` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
