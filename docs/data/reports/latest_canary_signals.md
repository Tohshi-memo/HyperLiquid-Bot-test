# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T10:37:34.882519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `0.2624` n `234`; crypto_major avg `0.2734` n `8`; equity avg `0.0941` n `142`; fx avg `0.0008` n `6`; index avg `0.0284` n `26`; metal avg `0.0688` n `20`; unknown avg `-0.1297` n `975`
- 1h: commodity avg `-0.0034` n `13`; crypto_alt avg `-0.5324` n `234`; crypto_major avg `-0.0893` n `8`; equity avg `0.0334` n `142`; fx avg `-0.0268` n `6`; index avg `0.0316` n `26`; metal avg `0.1116` n `20`; unknown avg `1.1774` n `973`
- 4h: commodity avg `0.2543` n `13`; crypto_alt avg `-1.4347` n `234`; crypto_major avg `-0.6859` n `8`; equity avg `-0.6248` n `142`; fx avg `-0.0295` n `6`; index avg `-0.1251` n `26`; metal avg `-0.213` n `20`; unknown avg `7.5916` n `956`
- 24h: commodity avg `-0.109` n `13`; crypto_alt avg `-0.9758` n `234`; crypto_major avg `-0.1329` n `8`; equity avg `0.4937` n `142`; fx avg `0.0355` n `6`; index avg `0.1805` n `26`; metal avg `-0.2476` n `20`; unknown avg `777.2986` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
