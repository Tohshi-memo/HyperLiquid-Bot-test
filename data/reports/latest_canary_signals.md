# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T07:07:29.858512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0415` n `12`; crypto_alt avg `0.0449` n `228`; crypto_major avg `0.0226` n `8`; equity avg `-0.0008` n `88`; fx avg `0.017` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0072` n `20`; unknown avg `0.2372` n `763`
- 1h: commodity avg `-0.1115` n `12`; crypto_alt avg `-0.0005` n `228`; crypto_major avg `-0.1312` n `8`; equity avg `-0.4244` n `88`; fx avg `-0.0188` n `6`; index avg `-0.0394` n `25`; metal avg `-0.0716` n `20`; unknown avg `0.7578` n `763`
- 4h: commodity avg `-0.1056` n `12`; crypto_alt avg `-0.1445` n `228`; crypto_major avg `-0.2766` n `8`; equity avg `-1.3482` n `88`; fx avg `-0.0435` n `6`; index avg `-0.313` n `25`; metal avg `-0.0288` n `20`; unknown avg `0.1737` n `739`
- 24h: commodity avg `-0.6384` n `12`; crypto_alt avg `2.2228` n `228`; crypto_major avg `1.6178` n `8`; equity avg `-2.2022` n `88`; fx avg `-0.0476` n `6`; index avg `-0.5584` n `25`; metal avg `1.2913` n `20`; unknown avg `25.0089` n `739`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
