# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T12:52:27.459589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `13`; crypto_alt avg `-0.0678` n `239`; crypto_major avg `-0.0283` n `8`; equity avg `-0.1359` n `162`; fx avg `-0.0132` n `6`; index avg `-0.0147` n `27`; metal avg `-0.0134` n `20`; unknown avg `36.5833` n `1262`
- 1h: commodity avg `0.1207` n `13`; crypto_alt avg `0.2274` n `239`; crypto_major avg `0.0783` n `8`; equity avg `-0.4153` n `162`; fx avg `-0.0159` n `6`; index avg `-0.0403` n `27`; metal avg `-0.0444` n `20`; unknown avg `43.9217` n `1254`
- 4h: commodity avg `0.0067` n `13`; crypto_alt avg `0.4446` n `239`; crypto_major avg `0.827` n `8`; equity avg `0.4205` n `162`; fx avg `-0.0317` n `6`; index avg `0.0622` n `27`; metal avg `0.0461` n `20`; unknown avg `46.0255` n `1200`
- 24h: commodity avg `0.9232` n `13`; crypto_alt avg `0.2992` n `239`; crypto_major avg `-1.4849` n `8`; equity avg `-0.42` n `162`; fx avg `-0.0143` n `6`; index avg `0.0497` n `27`; metal avg `-0.2847` n `20`; unknown avg `2.7333` n `1073`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
