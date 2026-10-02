# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T05:37:24.458516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `13`; crypto_alt avg `-0.0954` n `234`; crypto_major avg `-0.2773` n `8`; equity avg `-0.0917` n `142`; fx avg `-0.0122` n `6`; index avg `-0.0189` n `26`; metal avg `0.0064` n `20`; unknown avg `2.4834` n `985`
- 1h: commodity avg `0.013` n `13`; crypto_alt avg `-0.0113` n `234`; crypto_major avg `-0.2873` n `8`; equity avg `-0.0633` n `142`; fx avg `-0.0489` n `6`; index avg `-0.0094` n `26`; metal avg `0.0437` n `20`; unknown avg `2.3149` n `981`
- 4h: commodity avg `-0.0446` n `13`; crypto_alt avg `1.6324` n `234`; crypto_major avg `1.5928` n `8`; equity avg `0.3892` n `142`; fx avg `-0.0822` n `6`; index avg `0.0842` n `26`; metal avg `0.3545` n `20`; unknown avg `4.1937` n `975`
- 24h: commodity avg `0.453` n `13`; crypto_alt avg `0.0899` n `234`; crypto_major avg `0.7943` n `8`; equity avg `0.0608` n `142`; fx avg `-0.2605` n `6`; index avg `-0.0648` n `26`; metal avg `-0.1549` n `20`; unknown avg `0.2141` n `838`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
