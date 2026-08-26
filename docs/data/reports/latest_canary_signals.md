# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T16:08:55.678839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0308` n `12`; crypto_alt avg `0.0904` n `231`; crypto_major avg `0.1581` n `8`; equity avg `-0.0489` n `122`; fx avg `0.0065` n `6`; index avg `-0.0363` n `25`; metal avg `0.0249` n `20`; unknown avg `0.0601` n `797`
- 1h: commodity avg `0.2356` n `12`; crypto_alt avg `0.0427` n `231`; crypto_major avg `0.133` n `8`; equity avg `-0.1712` n `122`; fx avg `0.013` n `6`; index avg `-0.0311` n `25`; metal avg `-0.0843` n `20`; unknown avg `0.0934` n `797`
- 4h: commodity avg `0.5669` n `12`; crypto_alt avg `-1.0564` n `231`; crypto_major avg `-0.7911` n `8`; equity avg `-0.3357` n `122`; fx avg `-0.0087` n `6`; index avg `-0.026` n `25`; metal avg `-0.2756` n `20`; unknown avg `-0.1461` n `797`
- 24h: commodity avg `0.4361` n `12`; crypto_alt avg `-2.2991` n `231`; crypto_major avg `-2.1637` n `8`; equity avg `-0.662` n `122`; fx avg `-0.0409` n `6`; index avg `-0.0201` n `25`; metal avg `-0.2945` n `20`; unknown avg `0.2975` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1514`, n `670`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `670`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `670`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1015`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0999`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0926`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `670`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0845`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0701`, n `670`, weak_sample_signal
