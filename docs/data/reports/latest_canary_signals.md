# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T09:37:27.354507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `0.0223` n `230`; crypto_major avg `0.0138` n `8`; equity avg `0.0207` n `112`; fx avg `0.0002` n `6`; index avg `-0.0129` n `25`; metal avg `0.0028` n `20`; unknown avg `0.0074` n `784`
- 1h: commodity avg `0.0098` n `12`; crypto_alt avg `0.0253` n `230`; crypto_major avg `0.1583` n `8`; equity avg `0.0697` n `112`; fx avg `-0.0027` n `6`; index avg `0.0067` n `25`; metal avg `0.0225` n `20`; unknown avg `-0.0682` n `784`
- 4h: commodity avg `0.0409` n `12`; crypto_alt avg `0.2101` n `230`; crypto_major avg `0.2105` n `8`; equity avg `0.0957` n `112`; fx avg `0.0079` n `6`; index avg `-0.0108` n `25`; metal avg `0.0382` n `20`; unknown avg `0.1554` n `752`
- 24h: commodity avg `-0.0023` n `12`; crypto_alt avg `0.0204` n `230`; crypto_major avg `0.0863` n `8`; equity avg `0.698` n `112`; fx avg `-0.023` n `6`; index avg `0.0334` n `25`; metal avg `-0.0988` n `20`; unknown avg `0.1097` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
