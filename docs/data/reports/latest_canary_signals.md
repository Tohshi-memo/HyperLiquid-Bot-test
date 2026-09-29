# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T07:37:31.723783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1081` n `12`; crypto_alt avg `0.2118` n `234`; crypto_major avg `0.1538` n `8`; equity avg `0.1267` n `141`; fx avg `-0.0297` n `6`; index avg `0.0273` n `26`; metal avg `-0.0016` n `20`; unknown avg `1.6014` n `963`
- 1h: commodity avg `-0.1261` n `12`; crypto_alt avg `0.8756` n `234`; crypto_major avg `0.5333` n `8`; equity avg `0.2952` n `141`; fx avg `-0.0316` n `6`; index avg `0.0352` n `26`; metal avg `-0.0344` n `20`; unknown avg `1.5276` n `961`
- 4h: commodity avg `-0.1693` n `12`; crypto_alt avg `1.9658` n `234`; crypto_major avg `1.3181` n `8`; equity avg `0.6662` n `141`; fx avg `-0.0615` n `6`; index avg `0.0954` n `26`; metal avg `0.0072` n `20`; unknown avg `13.4291` n `937`
- 24h: commodity avg `-0.122` n `12`; crypto_alt avg `1.0845` n `234`; crypto_major avg `1.1915` n `8`; equity avg `-0.6009` n `141`; fx avg `-0.1286` n `6`; index avg `-0.0348` n `26`; metal avg `-0.1616` n `20`; unknown avg `57.5741` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
