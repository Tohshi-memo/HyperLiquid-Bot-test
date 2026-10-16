# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T22:07:29.982463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.018` n `13`; crypto_alt avg `0.1847` n `236`; crypto_major avg `0.0868` n `8`; equity avg `-0.0923` n `151`; fx avg `-0.0044` n `6`; index avg `-0.0101` n `26`; metal avg `0.0012` n `20`; unknown avg `0.9129` n `1191`
- 1h: commodity avg `-0.0425` n `13`; crypto_alt avg `0.3236` n `236`; crypto_major avg `0.2585` n `8`; equity avg `-0.2942` n `151`; fx avg `-0.0093` n `6`; index avg `-0.0271` n `26`; metal avg `0.0089` n `20`; unknown avg `0.5536` n `1191`
- 4h: commodity avg `0.0351` n `13`; crypto_alt avg `0.551` n `236`; crypto_major avg `0.5195` n `8`; equity avg `-0.6821` n `151`; fx avg `0.0131` n `6`; index avg `-0.0964` n `26`; metal avg `0.0219` n `20`; unknown avg `4.0483` n `1109`
- 24h: commodity avg `0.3707` n `13`; crypto_alt avg `-1.6353` n `236`; crypto_major avg `-1.4632` n `8`; equity avg `-4.2204` n `151`; fx avg `0.0133` n `6`; index avg `-0.6688` n `26`; metal avg `-0.0975` n `20`; unknown avg `8.4703` n `908`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1621`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1146`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0923`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0771`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0721`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0694`, n `666`, weak_sample_signal
