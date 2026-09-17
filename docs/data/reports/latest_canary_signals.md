# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T22:52:28.373268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `0.1033` n `234`; crypto_major avg `-0.0346` n `8`; equity avg `-0.0029` n `140`; fx avg `-0.0023` n `6`; index avg `-0.0038` n `26`; metal avg `-0.0233` n `20`; unknown avg `1.1793` n `899`
- 1h: commodity avg `0.0073` n `12`; crypto_alt avg `0.0519` n `234`; crypto_major avg `0.0844` n `8`; equity avg `-0.1119` n `140`; fx avg `0.0212` n `6`; index avg `-0.035` n `26`; metal avg `-0.0113` n `20`; unknown avg `1.3101` n `851`
- 4h: commodity avg `-0.129` n `12`; crypto_alt avg `0.2012` n `234`; crypto_major avg `0.2722` n `8`; equity avg `0.0223` n `140`; fx avg `-0.0011` n `6`; index avg `-0.0286` n `26`; metal avg `-0.0661` n `20`; unknown avg `0.2847` n `791`
- 24h: commodity avg `-0.1777` n `12`; crypto_alt avg `4.2737` n `234`; crypto_major avg `2.4916` n `8`; equity avg `1.9938` n `138`; fx avg `-0.0056` n `6`; index avg `0.3532` n `26`; metal avg `0.5464` n `20`; unknown avg `2.7011` n `757`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
