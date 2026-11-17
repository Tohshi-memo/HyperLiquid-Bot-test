# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T22:07:33.589203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `13`; crypto_alt avg `0.0842` n `239`; crypto_major avg `0.0673` n `8`; equity avg `0.3856` n `163`; fx avg `0.0009` n `6`; index avg `0.0301` n `27`; metal avg `0.0211` n `20`; unknown avg `271.7339` n `1253`
- 1h: commodity avg `0.007` n `13`; crypto_alt avg `0.2611` n `239`; crypto_major avg `0.3007` n `8`; equity avg `0.9681` n `163`; fx avg `-0.0157` n `6`; index avg `0.0829` n `27`; metal avg `0.0633` n `20`; unknown avg `1.5901` n `1257`
- 4h: commodity avg `-0.093` n `13`; crypto_alt avg `1.0597` n `239`; crypto_major avg `0.9661` n `8`; equity avg `1.6238` n `163`; fx avg `-0.0373` n `6`; index avg `0.1389` n `27`; metal avg `-0.0454` n `20`; unknown avg `1.3735` n `1231`
- 24h: commodity avg `0.3131` n `13`; crypto_alt avg `-0.1437` n `239`; crypto_major avg `-0.4466` n `8`; equity avg `0.0185` n `163`; fx avg `0.008` n `6`; index avg `-0.0072` n `27`; metal avg `-0.0157` n `20`; unknown avg `5.4976` n `1109`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
