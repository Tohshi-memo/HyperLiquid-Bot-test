# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T22:07:30.694091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `13`; crypto_alt avg `0.39` n `234`; crypto_major avg `0.3387` n `8`; equity avg `0.0673` n `142`; fx avg `-0.0016` n `6`; index avg `0.0115` n `26`; metal avg `-0.0125` n `20`; unknown avg `0.4923` n `967`
- 1h: commodity avg `0.0269` n `13`; crypto_alt avg `-0.2228` n `234`; crypto_major avg `-0.0881` n `8`; equity avg `-0.0139` n `142`; fx avg `0.0196` n `6`; index avg `0.003` n `26`; metal avg `-0.0181` n `20`; unknown avg `-0.1439` n `943`
- 4h: commodity avg `-0.0469` n `13`; crypto_alt avg `-0.306` n `234`; crypto_major avg `-0.1452` n `8`; equity avg `0.3392` n `142`; fx avg `0.009` n `6`; index avg `0.0937` n `26`; metal avg `0.1279` n `20`; unknown avg `-0.0472` n `891`
- 24h: commodity avg `0.1177` n `13`; crypto_alt avg `0.2946` n `234`; crypto_major avg `-0.0147` n `8`; equity avg `1.1252` n `142`; fx avg `-0.1013` n `6`; index avg `0.2184` n `26`; metal avg `-0.036` n `20`; unknown avg `0.0678` n `816`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
