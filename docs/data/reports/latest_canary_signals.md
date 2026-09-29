# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T06:22:29.518554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5292` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `0.2925` n `234`; crypto_major avg `0.2212` n `8`; equity avg `0.2762` n `141`; fx avg `0.0188` n `6`; index avg `0.0503` n `26`; metal avg `0.0265` n `20`; unknown avg `0.5968` n `963`
- 1h: commodity avg `-0.0644` n `12`; crypto_alt avg `0.6951` n `234`; crypto_major avg `0.6632` n `8`; equity avg `0.4269` n `141`; fx avg `-0.0077` n `6`; index avg `0.081` n `26`; metal avg `0.0645` n `20`; unknown avg `0.9924` n `945`
- 4h: commodity avg `0.0539` n `12`; crypto_alt avg `2.0783` n `234`; crypto_major avg `1.5324` n `8`; equity avg `0.1797` n `141`; fx avg `-0.0504` n `6`; index avg `-0.0019` n `26`; metal avg `0.0032` n `20`; unknown avg `1.8728` n `939`
- 24h: commodity avg `0.044` n `12`; crypto_alt avg `-0.6275` n `234`; crypto_major avg `0.5838` n `8`; equity avg `-1.5152` n `141`; fx avg `-0.1329` n `6`; index avg `-0.1279` n `26`; metal avg `-0.3393` n `20`; unknown avg `98.5382` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
