# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T15:52:28.757655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0388` n `13`; crypto_alt avg `0.1734` n `235`; crypto_major avg `0.0149` n `8`; equity avg `0.0448` n `150`; fx avg `0.0033` n `6`; index avg `0.0162` n `26`; metal avg `0.019` n `20`; unknown avg `0.0162` n `1058`
- 1h: commodity avg `-0.0003` n `13`; crypto_alt avg `0.1744` n `235`; crypto_major avg `-0.168` n `8`; equity avg `0.0468` n `150`; fx avg `-0.004` n `6`; index avg `-0.0031` n `26`; metal avg `0.0436` n `20`; unknown avg `0.8015` n `1026`
- 4h: commodity avg `0.4332` n `13`; crypto_alt avg `-0.3719` n `235`; crypto_major avg `-0.7238` n `8`; equity avg `-0.5445` n `150`; fx avg `0.0058` n `6`; index avg `-0.0753` n `26`; metal avg `0.0458` n `20`; unknown avg `0.3204` n `996`
- 24h: commodity avg `-0.0012` n `13`; crypto_alt avg `2.3831` n `235`; crypto_major avg `1.2872` n `8`; equity avg `0.1087` n `150`; fx avg `0.0183` n `6`; index avg `0.0494` n `26`; metal avg `0.7968` n `20`; unknown avg `1.1976` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
