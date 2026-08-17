# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T18:37:25.499353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0487` n `12`; crypto_alt avg `0.0983` n `230`; crypto_major avg `0.0518` n `8`; equity avg `0.0882` n `114`; fx avg `-0.0115` n `6`; index avg `-0.0047` n `25`; metal avg `-0.0747` n `20`; unknown avg `0.0537` n `792`
- 1h: commodity avg `0.0174` n `12`; crypto_alt avg `0.0794` n `230`; crypto_major avg `0.204` n `8`; equity avg `-0.0115` n `114`; fx avg `-0.0165` n `6`; index avg `-0.0215` n `25`; metal avg `-0.0705` n `20`; unknown avg `-0.0755` n `792`
- 4h: commodity avg `0.3683` n `12`; crypto_alt avg `0.1242` n `230`; crypto_major avg `0.3884` n `8`; equity avg `0.1664` n `114`; fx avg `0.0149` n `6`; index avg `-0.0784` n `25`; metal avg `-0.165` n `20`; unknown avg `0.1203` n `792`
- 24h: commodity avg `0.3151` n `12`; crypto_alt avg `0.0615` n `230`; crypto_major avg `1.0447` n `8`; equity avg `1.3486` n `114`; fx avg `0.0107` n `6`; index avg `0.1105` n `25`; metal avg `0.1308` n `20`; unknown avg `0.2407` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1666`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1598`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.153`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1359`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0998`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0845`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0833`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `669`, weak_sample_signal
