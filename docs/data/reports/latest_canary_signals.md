# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T13:07:25.815689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.063` n `231`; crypto_major avg `0.0144` n `8`; equity avg `-0.0266` n `127`; fx avg `0.0037` n `6`; index avg `-0.0053` n `26`; metal avg `0.0019` n `20`; unknown avg `0.0245` n `793`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `0.0769` n `231`; crypto_major avg `0.0523` n `8`; equity avg `-0.0599` n `127`; fx avg `-0.001` n `6`; index avg `-0.0087` n `26`; metal avg `0.0053` n `20`; unknown avg `0.1007` n `789`
- 4h: commodity avg `0.0181` n `12`; crypto_alt avg `0.1776` n `231`; crypto_major avg `0.1333` n `8`; equity avg `-0.0479` n `127`; fx avg `-0.0161` n `6`; index avg `-0.0071` n `26`; metal avg `0.0029` n `20`; unknown avg `0.0196` n `759`
- 24h: commodity avg `0.2069` n `12`; crypto_alt avg `-2.1248` n `231`; crypto_major avg `-2.0564` n `8`; equity avg `-1.4969` n `127`; fx avg `-0.0602` n `6`; index avg `-0.177` n `26`; metal avg `-0.8648` n `20`; unknown avg `-0.5402` n `743`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
