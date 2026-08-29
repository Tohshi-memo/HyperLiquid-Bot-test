# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T11:22:27.105273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `0.1002` n `231`; crypto_major avg `0.0484` n `8`; equity avg `0.0253` n `127`; fx avg `-0.0007` n `6`; index avg `0.0017` n `26`; metal avg `-0.0002` n `20`; unknown avg `-0.0751` n `781`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.0572` n `231`; crypto_major avg `-0.0428` n `8`; equity avg `0.0029` n `127`; fx avg `-0.0` n `6`; index avg `0.0028` n `26`; metal avg `-0.0146` n `20`; unknown avg `0.0059` n `779`
- 4h: commodity avg `0.0103` n `12`; crypto_alt avg `-0.2947` n `231`; crypto_major avg `0.0244` n `8`; equity avg `0.0146` n `127`; fx avg `-0.0122` n `6`; index avg `-0.008` n `26`; metal avg `-0.0021` n `20`; unknown avg `0.0015` n `777`
- 24h: commodity avg `0.0029` n `12`; crypto_alt avg `-2.5591` n `231`; crypto_major avg `-2.4339` n `8`; equity avg `-1.4431` n `127`; fx avg `-0.0888` n `6`; index avg `-0.1418` n `26`; metal avg `-0.7111` n `20`; unknown avg `-0.4009` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
