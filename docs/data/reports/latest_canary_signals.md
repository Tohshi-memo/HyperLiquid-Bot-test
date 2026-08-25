# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T13:07:25.203186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `-0.0613` n `231`; crypto_major avg `-0.0909` n `8`; equity avg `-0.0385` n `122`; fx avg `0.0107` n `6`; index avg `-0.0066` n `25`; metal avg `-0.1296` n `20`; unknown avg `-0.0156` n `795`
- 1h: commodity avg `-0.038` n `12`; crypto_alt avg `0.3857` n `231`; crypto_major avg `0.2869` n `8`; equity avg `-0.0884` n `122`; fx avg `0.0283` n `6`; index avg `-0.0356` n `25`; metal avg `-0.1052` n `20`; unknown avg `0.1247` n `795`
- 4h: commodity avg `-0.2471` n `12`; crypto_alt avg `-0.6407` n `231`; crypto_major avg `-0.9627` n `8`; equity avg `-0.0438` n `122`; fx avg `-0.0132` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0157` n `20`; unknown avg `-0.0266` n `794`
- 24h: commodity avg `-1.0696` n `12`; crypto_alt avg `-1.3029` n `231`; crypto_major avg `-0.91` n `8`; equity avg `0.5755` n `122`; fx avg `0.0267` n `6`; index avg `0.1339` n `25`; metal avg `-0.5217` n `20`; unknown avg `-0.9548` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
