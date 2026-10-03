# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T00:22:32.098518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0273` n `13`; crypto_alt avg `0.2154` n `235`; crypto_major avg `0.1888` n `8`; equity avg `-0.0087` n `143`; fx avg `0.008` n `6`; index avg `0.0067` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.2095` n `984`
- 1h: commodity avg `-0.0089` n `13`; crypto_alt avg `0.6929` n `235`; crypto_major avg `0.3987` n `8`; equity avg `0.052` n `143`; fx avg `-0.0025` n `6`; index avg `0.0152` n `26`; metal avg `-0.0104` n `20`; unknown avg `0.4523` n `976`
- 4h: commodity avg `0.1137` n `13`; crypto_alt avg `1.7245` n `235`; crypto_major avg `0.9444` n `8`; equity avg `0.0731` n `143`; fx avg `-0.0051` n `6`; index avg `0.0012` n `26`; metal avg `-0.01` n `20`; unknown avg `1.6827` n `948`
- 24h: commodity avg `0.1152` n `13`; crypto_alt avg `-0.4354` n `235`; crypto_major avg `-0.2621` n `8`; equity avg `0.5351` n `142`; fx avg `-0.1994` n `6`; index avg `0.2498` n `26`; metal avg `-0.2178` n `20`; unknown avg `-0.4197` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
