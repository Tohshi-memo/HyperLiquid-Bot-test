# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T09:37:31.859430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `-0.5438` n `234`; crypto_major avg `-0.3635` n `8`; equity avg `0.0024` n `141`; fx avg `-0.0092` n `6`; index avg `-0.0076` n `26`; metal avg `-0.005` n `20`; unknown avg `-0.3904` n `962`
- 1h: commodity avg `0.093` n `12`; crypto_alt avg `-0.3531` n `234`; crypto_major avg `-0.1501` n `8`; equity avg `-0.1876` n `141`; fx avg `0.0342` n `6`; index avg `-0.0158` n `26`; metal avg `0.016` n `20`; unknown avg `10.7368` n `958`
- 4h: commodity avg `0.1875` n `12`; crypto_alt avg `-0.9635` n `234`; crypto_major avg `-0.117` n `8`; equity avg `-1.1626` n `141`; fx avg `-0.07` n `6`; index avg `-0.097` n `26`; metal avg `-0.1789` n `20`; unknown avg `9.6298` n `918`
- 24h: commodity avg `-0.0866` n `12`; crypto_alt avg `-4.4416` n `234`; crypto_major avg `-3.2621` n `8`; equity avg `-2.912` n `141`; fx avg `0.015` n `6`; index avg `-0.2855` n `26`; metal avg `-0.9855` n `20`; unknown avg `6.1469` n `813`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
