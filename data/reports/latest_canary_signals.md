# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T09:52:28.469076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `-0.1461` n `234`; crypto_major avg `0.0225` n `8`; equity avg `0.1173` n `141`; fx avg `-0.0104` n `6`; index avg `0.0179` n `26`; metal avg `0.0745` n `20`; unknown avg `0.0466` n `962`
- 1h: commodity avg `0.0843` n `12`; crypto_alt avg `-0.6052` n `234`; crypto_major avg `-0.2855` n `8`; equity avg `0.0218` n `141`; fx avg `-0.0152` n `6`; index avg `0.0147` n `26`; metal avg `0.0786` n `20`; unknown avg `-0.0393` n `958`
- 4h: commodity avg `0.2231` n `12`; crypto_alt avg `-1.542` n `234`; crypto_major avg `-0.425` n `8`; equity avg `-1.0174` n `141`; fx avg `-0.0898` n `6`; index avg `-0.0613` n `26`; metal avg `-0.1032` n `20`; unknown avg `14.5164` n `918`
- 24h: commodity avg `-0.0747` n `12`; crypto_alt avg `-4.6128` n `234`; crypto_major avg `-3.3994` n `8`; equity avg `-2.8183` n `141`; fx avg `0.0032` n `6`; index avg `-0.2676` n `26`; metal avg `-0.9174` n `20`; unknown avg `6.2687` n `814`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
