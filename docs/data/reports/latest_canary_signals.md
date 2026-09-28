# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T22:37:36.144887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0204` n `12`; crypto_alt avg `0.3893` n `234`; crypto_major avg `0.3842` n `8`; equity avg `0.0237` n `141`; fx avg `-0.0018` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0285` n `20`; unknown avg `0.188` n `963`
- 1h: commodity avg `-0.0846` n `12`; crypto_alt avg `-0.1318` n `234`; crypto_major avg `-0.089` n `8`; equity avg `0.022` n `141`; fx avg `0.0078` n `6`; index avg `0.0043` n `26`; metal avg `0.0341` n `20`; unknown avg `-0.2772` n `937`
- 4h: commodity avg `0.2576` n `12`; crypto_alt avg `-0.9871` n `234`; crypto_major avg `-0.8986` n `8`; equity avg `-0.2266` n `141`; fx avg `0.002` n `6`; index avg `-0.0238` n `26`; metal avg `-0.1376` n `20`; unknown avg `0.21` n `833`
- 24h: commodity avg `0.0409` n `12`; crypto_alt avg `-3.4197` n `234`; crypto_major avg `-1.5618` n `8`; equity avg `-2.9301` n `141`; fx avg `0.0536` n `6`; index avg `-0.1984` n `26`; metal avg `-0.9513` n `20`; unknown avg `53.3009` n `800`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
