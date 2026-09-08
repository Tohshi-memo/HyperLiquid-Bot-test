# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T07:52:31.303515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `11`; crypto_alt avg `-0.3127` n `232`; crypto_major avg `-0.3113` n `8`; equity avg `-0.1613` n `123`; fx avg `-0.0196` n `5`; index avg `-0.0421` n `20`; metal avg `-0.0503` n `18`; unknown avg `2.5584` n `795`
- 1h: commodity avg `0.0692` n `11`; crypto_alt avg `0.3061` n `232`; crypto_major avg `0.2553` n `8`; equity avg `-0.089` n `123`; fx avg `-0.0444` n `5`; index avg `-0.0562` n `20`; metal avg `-0.0812` n `18`; unknown avg `0.6305` n `793`
- 4h: commodity avg `0.3072` n `11`; crypto_alt avg `-0.3056` n `232`; crypto_major avg `-0.282` n `8`; equity avg `-1.1105` n `123`; fx avg `0.1118` n `5`; index avg `-0.3794` n `20`; metal avg `-0.3028` n `18`; unknown avg `0.8762` n `745`
- 24h: commodity avg `0.5289` n `11`; crypto_alt avg `0.9715` n `232`; crypto_major avg `-0.7921` n `8`; equity avg `-0.3154` n `123`; fx avg `-0.2591` n `5`; index avg `-0.1879` n `20`; metal avg `0.0317` n `18`; unknown avg `7530.8146` n `664`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
