# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T03:22:38.293893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `13`; crypto_alt avg `0.2966` n `235`; crypto_major avg `0.0832` n `8`; equity avg `-0.0077` n `143`; fx avg `-0.0013` n `6`; index avg `0.0001` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.0554` n `984`
- 1h: commodity avg `0.0114` n `13`; crypto_alt avg `0.1101` n `235`; crypto_major avg `-0.1842` n `8`; equity avg `-0.0461` n `143`; fx avg `-0.004` n `6`; index avg `-0.0049` n `26`; metal avg `-0.0092` n `20`; unknown avg `-0.1754` n `982`
- 4h: commodity avg `-0.2024` n `13`; crypto_alt avg `0.9113` n `235`; crypto_major avg `0.2575` n `8`; equity avg `0.0291` n `143`; fx avg `0.0078` n `6`; index avg `0.0351` n `26`; metal avg `-0.0223` n `20`; unknown avg `-0.1877` n `976`
- 24h: commodity avg `0.0918` n `13`; crypto_alt avg `-0.3778` n `235`; crypto_major avg `-0.8447` n `8`; equity avg `0.576` n `142`; fx avg `-0.1244` n `6`; index avg `0.2663` n `26`; metal avg `-0.2263` n `20`; unknown avg `-0.7962` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
