# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T09:22:29.683753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0096` n `12`; crypto_alt avg `0.6752` n `234`; crypto_major avg `0.4855` n `8`; equity avg `0.0148` n `141`; fx avg `-0.0037` n `6`; index avg `0.0195` n `26`; metal avg `0.0143` n `20`; unknown avg `0.5606` n `962`
- 1h: commodity avg `0.1077` n `12`; crypto_alt avg `-0.009` n `234`; crypto_major avg `0.1285` n `8`; equity avg `-0.2504` n `141`; fx avg `0.046` n `6`; index avg `-0.0187` n `26`; metal avg `-0.0388` n `20`; unknown avg `9.3568` n `958`
- 4h: commodity avg `0.1894` n `12`; crypto_alt avg `-0.9849` n `234`; crypto_major avg `-0.3429` n `8`; equity avg `-1.2185` n `141`; fx avg `-0.0689` n `6`; index avg `-0.0878` n `26`; metal avg `-0.1962` n `20`; unknown avg `7.9546` n `918`
- 24h: commodity avg `-0.078` n `12`; crypto_alt avg `-3.6678` n `234`; crypto_major avg `-2.7719` n `8`; equity avg `-2.8894` n `141`; fx avg `0.0198` n `6`; index avg `-0.2748` n `26`; metal avg `-0.9765` n `20`; unknown avg `6.0123` n `813`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
