# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T11:07:27.844187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.0568` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0333` n `12`; crypto_alt avg `0.0144` n `229`; crypto_major avg `0.041` n `8`; equity avg `0.0878` n `88`; fx avg `-0.003` n `6`; index avg `0.0057` n `25`; metal avg `-0.0858` n `20`; unknown avg `0.0153` n `763`
- 1h: commodity avg `-0.037` n `12`; crypto_alt avg `0.0778` n `229`; crypto_major avg `0.5925` n `8`; equity avg `0.2078` n `88`; fx avg `0.0097` n `6`; index avg `0.0356` n `25`; metal avg `-0.1339` n `20`; unknown avg `0.0776` n `763`
- 4h: commodity avg `0.011` n `12`; crypto_alt avg `1.3497` n `228`; crypto_major avg `2.0039` n `8`; equity avg `0.642` n `88`; fx avg `-0.0289` n `6`; index avg `0.0532` n `25`; metal avg `-0.0529` n `20`; unknown avg `1.1636` n `763`
- 24h: commodity avg `-0.4948` n `12`; crypto_alt avg `2.9606` n `228`; crypto_major avg `3.9927` n `8`; equity avg `-1.9584` n `88`; fx avg `-0.12` n `6`; index avg `-0.5697` n `25`; metal avg `0.7878` n `20`; unknown avg `3.2045` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
