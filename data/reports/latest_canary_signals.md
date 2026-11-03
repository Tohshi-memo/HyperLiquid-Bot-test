# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T16:37:46.344043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0143` n `13`; crypto_alt avg `0.2063` n `239`; crypto_major avg `0.2192` n `8`; equity avg `-0.1116` n `158`; fx avg `-0.0049` n `6`; index avg `-0.007` n `27`; metal avg `-0.0261` n `20`; unknown avg `0.8177` n `1263`
- 1h: commodity avg `-0.0183` n `13`; crypto_alt avg `0.1099` n `239`; crypto_major avg `0.1089` n `8`; equity avg `-0.2462` n `158`; fx avg `0.0109` n `6`; index avg `-0.0177` n `27`; metal avg `-0.0164` n `20`; unknown avg `0.2522` n `1251`
- 4h: commodity avg `-0.3001` n `13`; crypto_alt avg `-0.1403` n `239`; crypto_major avg `0.2228` n `8`; equity avg `0.7236` n `158`; fx avg `0.0432` n `6`; index avg `0.0735` n `27`; metal avg `0.0443` n `20`; unknown avg `5.5419` n `1249`
- 24h: commodity avg `-0.1345` n `13`; crypto_alt avg `-0.2747` n `239`; crypto_major avg `0.3845` n `8`; equity avg `-0.8967` n `158`; fx avg `0.0404` n `6`; index avg `-0.1008` n `27`; metal avg `-0.6455` n `20`; unknown avg `0.1368` n `1021`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
