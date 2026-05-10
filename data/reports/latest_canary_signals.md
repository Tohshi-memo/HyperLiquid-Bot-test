# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T01:37:13.178292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `0.0214` n `228`; crypto_major avg `0.017` n `8`; equity avg `0.0221` n `65`; fx avg `0.0` n `5`; index avg `0.0071` n `23`; metal avg `0.0017` n `18`; unknown avg `-0.0109` n `376`
- 1h: commodity avg `0.0114` n `12`; crypto_alt avg `-0.6967` n `228`; crypto_major avg `-0.4204` n `8`; equity avg `-0.0269` n `65`; fx avg `0.0002` n `5`; index avg `0.0385` n `23`; metal avg `-0.0079` n `18`; unknown avg `-0.3157` n `376`
- 4h: commodity avg `-0.05` n `12`; crypto_alt avg `-1.1528` n `228`; crypto_major avg `-0.6568` n `8`; equity avg `0.1514` n `65`; fx avg `0.0002` n `5`; index avg `0.1238` n `23`; metal avg `0.0608` n `18`; unknown avg `-0.6351` n `376`
- 24h: commodity avg `0.5348` n `12`; crypto_alt avg `-2.1334` n `228`; crypto_major avg `-1.0028` n `8`; equity avg `0.6848` n `65`; fx avg `-0.0287` n `5`; index avg `0.4168` n `23`; metal avg `0.2353` n `18`; unknown avg `-0.4914` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
