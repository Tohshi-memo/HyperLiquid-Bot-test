# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T12:37:32.458192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `12`; crypto_alt avg `-0.0068` n `234`; crypto_major avg `0.5538` n `8`; equity avg `-0.0248` n `141`; fx avg `-0.0075` n `6`; index avg `-0.0234` n `26`; metal avg `-0.0292` n `20`; unknown avg `206.2199` n `963`
- 1h: commodity avg `-0.1277` n `12`; crypto_alt avg `0.2913` n `234`; crypto_major avg `0.7246` n `8`; equity avg `0.0637` n `141`; fx avg `-0.0219` n `6`; index avg `-0.0027` n `26`; metal avg `-0.0927` n `20`; unknown avg `207.4077` n `955`
- 4h: commodity avg `-0.3181` n `12`; crypto_alt avg `1.2017` n `234`; crypto_major avg `1.1257` n `8`; equity avg `0.2221` n `141`; fx avg `-0.0389` n `6`; index avg `0.041` n `26`; metal avg `0.107` n `20`; unknown avg `199.6461` n `955`
- 24h: commodity avg `-0.6448` n `12`; crypto_alt avg `0.9859` n `234`; crypto_major avg `0.9276` n `8`; equity avg `-0.164` n `141`; fx avg `-0.1214` n `6`; index avg `-0.0393` n `26`; metal avg `-0.1394` n `20`; unknown avg `75.2648` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
