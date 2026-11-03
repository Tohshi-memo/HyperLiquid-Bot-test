# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T21:07:59.046401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0479` n `13`; crypto_alt avg `0.1038` n `239`; crypto_major avg `0.0744` n `8`; equity avg `0.2269` n `158`; fx avg `-0.0002` n `6`; index avg `0.0245` n `27`; metal avg `0.0144` n `20`; unknown avg `0.4099` n `1249`
- 1h: commodity avg `-0.0035` n `13`; crypto_alt avg `0.2534` n `239`; crypto_major avg `0.2795` n `8`; equity avg `0.3662` n `158`; fx avg `0.0026` n `6`; index avg `0.0356` n `27`; metal avg `0.0297` n `20`; unknown avg `0.4255` n `1231`
- 4h: commodity avg `0.3054` n `13`; crypto_alt avg `-0.0862` n `239`; crypto_major avg `-0.0866` n `8`; equity avg `0.0039` n `158`; fx avg `0.0122` n `6`; index avg `-0.0298` n `27`; metal avg `-0.1078` n `20`; unknown avg `0.2896` n `1175`
- 24h: commodity avg `0.4331` n `13`; crypto_alt avg `1.2356` n `239`; crypto_major avg `1.5851` n `8`; equity avg `1.8931` n `158`; fx avg `0.0749` n `6`; index avg `0.1681` n `27`; metal avg `-0.5146` n `20`; unknown avg `375.8465` n `1043`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
