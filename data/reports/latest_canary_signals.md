# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T12:52:27.722898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3666` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.3396` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1529` n `12`; crypto_alt avg `-0.0848` n `228`; crypto_major avg `-0.1529` n `8`; equity avg `-0.0365` n `88`; fx avg `0.0206` n `6`; index avg `0.0161` n `23`; metal avg `-0.0321` n `20`; unknown avg `0.0154` n `765`
- 1h: commodity avg `0.0336` n `12`; crypto_alt avg `-0.9843` n `228`; crypto_major avg `-1.4033` n `8`; equity avg `-0.5979` n `88`; fx avg `-0.0006` n `6`; index avg `-0.0367` n `23`; metal avg `-0.3163` n `20`; unknown avg `-0.0997` n `765`
- 4h: commodity avg `0.1969` n `12`; crypto_alt avg `-1.36` n `228`; crypto_major avg `-1.2962` n `8`; equity avg `-0.2074` n `88`; fx avg `-0.0189` n `6`; index avg `0.0434` n `23`; metal avg `-0.0224` n `20`; unknown avg `-0.2527` n `765`
- 24h: commodity avg `0.3853` n `12`; crypto_alt avg `-2.2881` n `228`; crypto_major avg `-1.2397` n `8`; equity avg `0.9673` n `88`; fx avg `0.075` n `6`; index avg `0.18` n `23`; metal avg `-0.0829` n `20`; unknown avg `8.8545` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
