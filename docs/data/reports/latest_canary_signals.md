# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T02:07:25.882653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `-0.088` n `228`; crypto_major avg `-0.0701` n `8`; equity avg `-0.0042` n `78`; fx avg `-0.0123` n `6`; index avg `0.0006` n `23`; metal avg `-0.002` n `18`; unknown avg `-0.3603` n `702`
- 1h: commodity avg `-0.0184` n `12`; crypto_alt avg `0.1506` n `228`; crypto_major avg `0.0459` n `8`; equity avg `0.0291` n `78`; fx avg `-0.0071` n `6`; index avg `-0.012` n `23`; metal avg `0.0183` n `18`; unknown avg `0.1429` n `701`
- 4h: commodity avg `0.0125` n `12`; crypto_alt avg `0.7425` n `228`; crypto_major avg `0.2988` n `8`; equity avg `0.1087` n `78`; fx avg `-0.0108` n `6`; index avg `0.0077` n `23`; metal avg `-0.0104` n `18`; unknown avg `1.18` n `701`
- 24h: commodity avg `0.1857` n `12`; crypto_alt avg `1.5362` n `228`; crypto_major avg `1.5201` n `8`; equity avg `0.515` n `78`; fx avg `0.0423` n `6`; index avg `0.0097` n `23`; metal avg `-0.0394` n `18`; unknown avg `1.6953` n `557`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
