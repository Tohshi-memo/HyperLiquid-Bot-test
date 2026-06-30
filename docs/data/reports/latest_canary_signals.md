# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T13:07:26.509528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3768` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1264` n `12`; crypto_alt avg `0.007` n `228`; crypto_major avg `0.0537` n `8`; equity avg `-0.1173` n `88`; fx avg `-0.0003` n `6`; index avg `-0.0185` n `23`; metal avg `0.078` n `20`; unknown avg `-0.0217` n `765`
- 1h: commodity avg `0.1081` n `12`; crypto_alt avg `-0.4574` n `228`; crypto_major avg `-0.6815` n `8`; equity avg `-0.5007` n `88`; fx avg `-0.0012` n `6`; index avg `-0.0203` n `23`; metal avg `-0.1857` n `20`; unknown avg `-0.0207` n `765`
- 4h: commodity avg `0.3461` n `12`; crypto_alt avg `-1.4822` n `228`; crypto_major avg `-1.3565` n `8`; equity avg `-0.4885` n `88`; fx avg `-0.0014` n `6`; index avg `0.0203` n `23`; metal avg `-0.0143` n `20`; unknown avg `-0.1049` n `765`
- 24h: commodity avg `0.5513` n `12`; crypto_alt avg `-2.6934` n `228`; crypto_major avg `-1.8059` n `8`; equity avg `0.6877` n `88`; fx avg `0.0936` n `6`; index avg `0.1387` n `23`; metal avg `-0.0434` n `20`; unknown avg `8.9407` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
