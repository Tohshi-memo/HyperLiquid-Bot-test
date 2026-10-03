# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T00:07:31.384476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0609` n `13`; crypto_alt avg `-0.0132` n `235`; crypto_major avg `-0.0664` n `8`; equity avg `0.0172` n `143`; fx avg `-0.0041` n `6`; index avg `0.0052` n `26`; metal avg `0.0008` n `20`; unknown avg `-0.0799` n `976`
- 1h: commodity avg `0.0055` n `13`; crypto_alt avg `0.7066` n `235`; crypto_major avg `0.2676` n `8`; equity avg `0.0572` n `143`; fx avg `-0.0109` n `6`; index avg `0.0061` n `26`; metal avg `-0.0095` n `20`; unknown avg `0.1593` n `976`
- 4h: commodity avg `0.1435` n `13`; crypto_alt avg `1.4832` n `235`; crypto_major avg `0.7491` n `8`; equity avg `0.0572` n `143`; fx avg `-0.0245` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0114` n `20`; unknown avg `0.7459` n `918`
- 24h: commodity avg `0.156` n `13`; crypto_alt avg `-0.3374` n `235`; crypto_major avg `-0.338` n `8`; equity avg `0.7769` n `142`; fx avg `-0.1761` n `6`; index avg `0.2971` n `26`; metal avg `-0.2458` n `20`; unknown avg `-0.3703` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
