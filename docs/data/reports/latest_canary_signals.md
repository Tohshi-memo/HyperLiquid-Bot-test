# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T18:22:26.302153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.056` n `12`; crypto_alt avg `-0.0103` n `230`; crypto_major avg `0.054` n `8`; equity avg `-0.1027` n `114`; fx avg `-0.0046` n `6`; index avg `-0.0167` n `25`; metal avg `-0.0219` n `20`; unknown avg `-0.0497` n `792`
- 1h: commodity avg `0.1871` n `12`; crypto_alt avg `-0.2462` n `230`; crypto_major avg `-0.1206` n `8`; equity avg `-0.196` n `114`; fx avg `-0.0015` n `6`; index avg `-0.0447` n `25`; metal avg `-0.0401` n `20`; unknown avg `-0.0178` n `792`
- 4h: commodity avg `0.4016` n `12`; crypto_alt avg `0.0552` n `230`; crypto_major avg `0.3906` n `8`; equity avg `0.1718` n `114`; fx avg `0.0153` n `6`; index avg `-0.043` n `25`; metal avg `-0.027` n `20`; unknown avg `0.1663` n `792`
- 24h: commodity avg `0.3706` n `12`; crypto_alt avg `0.0061` n `230`; crypto_major avg `0.997` n `8`; equity avg `1.241` n `114`; fx avg `0.0301` n `6`; index avg `0.1128` n `25`; metal avg `0.2029` n `20`; unknown avg `0.2893` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1672`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.156`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1532`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1009`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0833`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0819`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `669`, weak_sample_signal
