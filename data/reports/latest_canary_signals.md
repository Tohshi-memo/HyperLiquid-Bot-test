# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T15:37:23.844867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0825` n `12`; crypto_alt avg `-0.1194` n `228`; crypto_major avg `-0.3158` n `8`; equity avg `-1.1134` n `67`; fx avg `-0.0225` n `6`; index avg `-0.0752` n `23`; metal avg `0.0345` n `18`; unknown avg `0.8866` n `385`
- 1h: commodity avg `0.4525` n `12`; crypto_alt avg `0.3171` n `228`; crypto_major avg `-0.0105` n `8`; equity avg `0.0723` n `67`; fx avg `-0.0093` n `6`; index avg `-0.082` n `23`; metal avg `0.1627` n `18`; unknown avg `0.6896` n `385`
- 4h: commodity avg `0.36` n `12`; crypto_alt avg `1.058` n `228`; crypto_major avg `1.1808` n `8`; equity avg `0.2891` n `67`; fx avg `-0.0799` n `6`; index avg `-0.0983` n `23`; metal avg `0.5189` n `18`; unknown avg `1.5391` n `385`
- 24h: commodity avg `0.7383` n `12`; crypto_alt avg `1.304` n `228`; crypto_major avg `2.3336` n `8`; equity avg `0.6662` n `66`; fx avg `-0.0078` n `6`; index avg `0.1531` n `23`; metal avg `-0.4953` n `18`; unknown avg `7.862` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0455`, n `668`, weak_sample_signal
