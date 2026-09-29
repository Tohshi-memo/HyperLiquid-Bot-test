# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T07:07:30.640814+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6709` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0228` n `12`; crypto_alt avg `0.373` n `234`; crypto_major avg `0.2366` n `8`; equity avg `0.0937` n `141`; fx avg `-0.0154` n `6`; index avg `-0.0074` n `26`; metal avg `0.0028` n `20`; unknown avg `0.4485` n `961`
- 1h: commodity avg `-0.0042` n `12`; crypto_alt avg `0.9354` n `234`; crypto_major avg `0.5959` n `8`; equity avg `0.4798` n `141`; fx avg `0.0196` n `6`; index avg `0.0802` n `26`; metal avg `0.0402` n `20`; unknown avg `0.7529` n `959`
- 4h: commodity avg `-0.0441` n `12`; crypto_alt avg `2.4638` n `234`; crypto_major avg `1.6778` n `8`; equity avg `0.5897` n `141`; fx avg `-0.0467` n `6`; index avg `0.0786` n `26`; metal avg `0.0069` n `20`; unknown avg `1.6287` n `937`
- 24h: commodity avg `0.0536` n `12`; crypto_alt avg `0.0331` n `234`; crypto_major avg `0.9059` n `8`; equity avg `-0.8238` n `141`; fx avg `-0.1051` n `6`; index avg `-0.0794` n `26`; metal avg `-0.1958` n `20`; unknown avg `57.2547` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
