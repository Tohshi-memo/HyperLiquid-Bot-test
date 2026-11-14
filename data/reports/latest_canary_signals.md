# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T07:07:30.374066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `13`; crypto_alt avg `-0.0574` n `239`; crypto_major avg `-0.0188` n `8`; equity avg `-0.0107` n `162`; fx avg `0.0096` n `6`; index avg `-0.0012` n `27`; metal avg `0.0064` n `20`; unknown avg `0.7495` n `1254`
- 1h: commodity avg `0.0412` n `13`; crypto_alt avg `-0.6188` n `239`; crypto_major avg `-0.0933` n `8`; equity avg `-0.0626` n `162`; fx avg `-0.0105` n `6`; index avg `-0.0141` n `27`; metal avg `0.0074` n `20`; unknown avg `11.6308` n `1250`
- 4h: commodity avg `-0.0095` n `13`; crypto_alt avg `-0.6003` n `239`; crypto_major avg `-0.4872` n `8`; equity avg `0.0264` n `162`; fx avg `-0.0097` n `6`; index avg `-0.0022` n `27`; metal avg `0.005` n `20`; unknown avg `5.0778` n `1214`
- 24h: commodity avg `-0.1367` n `13`; crypto_alt avg `-2.4985` n `239`; crypto_major avg `-2.7599` n `8`; equity avg `-2.6896` n `162`; fx avg `-0.1436` n `6`; index avg `-0.2246` n `27`; metal avg `-0.4695` n `20`; unknown avg `65.071` n `1018`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
