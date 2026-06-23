# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T10:37:29.372947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5951` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.499` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0289` n `12`; crypto_alt avg `-0.2501` n `228`; crypto_major avg `-0.1992` n `8`; equity avg `-0.3309` n `86`; fx avg `0.009` n `6`; index avg `-0.0762` n `23`; metal avg `-0.076` n `20`; unknown avg `-0.0625` n `764`
- 1h: commodity avg `0.12` n `12`; crypto_alt avg `-0.1493` n `228`; crypto_major avg `-0.1332` n `8`; equity avg `-0.3` n `86`; fx avg `-0.0181` n `6`; index avg `-0.0936` n `23`; metal avg `0.0114` n `20`; unknown avg `-0.1101` n `764`
- 4h: commodity avg `0.1491` n `12`; crypto_alt avg `-0.9572` n `228`; crypto_major avg `-1.4853` n `8`; equity avg `-0.19` n `86`; fx avg `-0.1154` n `6`; index avg `0.0137` n `23`; metal avg `0.1098` n `20`; unknown avg `-0.4887` n `620`
- 24h: commodity avg `-0.6037` n `12`; crypto_alt avg `-4.0037` n `228`; crypto_major avg `-4.206` n `8`; equity avg `-4.5234` n `85`; fx avg `-0.1349` n `6`; index avg `-0.9031` n `23`; metal avg `-1.2632` n `20`; unknown avg `0.6614` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
