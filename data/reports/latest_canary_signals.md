# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T12:16:05.236482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0353` n `12`; crypto_alt avg `-0.0493` n `230`; crypto_major avg `-0.0885` n `8`; equity avg `-0.1775` n `114`; fx avg `0.0014` n `6`; index avg `-0.0216` n `25`; metal avg `-0.0029` n `20`; unknown avg `0.0089` n `795`
- 1h: commodity avg `0.1257` n `12`; crypto_alt avg `-0.0847` n `230`; crypto_major avg `-0.1377` n `8`; equity avg `-0.1521` n `114`; fx avg `0.0081` n `6`; index avg `-0.0169` n `25`; metal avg `-0.0338` n `20`; unknown avg `-0.0593` n `795`
- 4h: commodity avg `0.0393` n `12`; crypto_alt avg `0.2519` n `230`; crypto_major avg `0.2535` n `8`; equity avg `-0.0349` n `114`; fx avg `-0.0384` n `6`; index avg `0.0035` n `25`; metal avg `0.0398` n `20`; unknown avg `-0.0688` n `795`
- 24h: commodity avg `0.6932` n `12`; crypto_alt avg `-0.7315` n `230`; crypto_major avg `0.1876` n `8`; equity avg `-2.3913` n `114`; fx avg `-0.0426` n `6`; index avg `-0.5062` n `25`; metal avg `-0.1746` n `20`; unknown avg `-0.0872` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
