# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T23:55:57.012917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0323` n `12`; crypto_alt avg `-0.06` n `228`; crypto_major avg `-0.0764` n `8`; equity avg `-0.0331` n `88`; fx avg `0.0111` n `6`; index avg `-0.0197` n `23`; metal avg `0.0423` n `20`; unknown avg `-0.0353` n `764`
- 1h: commodity avg `-0.1082` n `12`; crypto_alt avg `0.6776` n `228`; crypto_major avg `0.9729` n `8`; equity avg `0.0882` n `88`; fx avg `0.0057` n `6`; index avg `-0.0381` n `23`; metal avg `0.0264` n `20`; unknown avg `0.6505` n `762`
- 4h: commodity avg `-0.5326` n `12`; crypto_alt avg `0.2018` n `228`; crypto_major avg `0.476` n `8`; equity avg `0.339` n `88`; fx avg `-0.0391` n `6`; index avg `0.0982` n `23`; metal avg `-0.1136` n `20`; unknown avg `0.8746` n `762`
- 24h: commodity avg `-0.3217` n `12`; crypto_alt avg `-0.2715` n `228`; crypto_major avg `-0.3307` n `8`; equity avg `0.4295` n `88`; fx avg `-0.0819` n `6`; index avg `0.1044` n `23`; metal avg `-0.1283` n `20`; unknown avg `15.3043` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
