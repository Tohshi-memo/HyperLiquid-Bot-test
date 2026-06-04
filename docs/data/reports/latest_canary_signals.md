# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T21:37:20.718588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.213` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0942` n `12`; crypto_alt avg `-0.9295` n `228`; crypto_major avg `-0.6318` n `8`; equity avg `-0.0386` n `74`; fx avg `-0.0058` n `6`; index avg `0.1112` n `23`; metal avg `0.027` n `18`; unknown avg `0.7766` n `424`
- 1h: commodity avg `0.1868` n `12`; crypto_alt avg `-1.5918` n `228`; crypto_major avg `-1.1578` n `8`; equity avg `-0.0444` n `74`; fx avg `0.0177` n `6`; index avg `0.0552` n `23`; metal avg `-0.0129` n `18`; unknown avg `0.5157` n `424`
- 4h: commodity avg `0.5503` n `12`; crypto_alt avg `-1.8206` n `228`; crypto_major avg `-0.7761` n `8`; equity avg `-0.8058` n `74`; fx avg `-0.0149` n `6`; index avg `-0.0876` n `23`; metal avg `-0.2058` n `18`; unknown avg `0.0119` n `424`
- 24h: commodity avg `-0.7184` n `12`; crypto_alt avg `-7.0944` n `228`; crypto_major avg `-4.942` n `8`; equity avg `-0.0318` n `73`; fx avg `0.0683` n `6`; index avg `0.3625` n `23`; metal avg `0.8218` n `18`; unknown avg `-0.2971` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
