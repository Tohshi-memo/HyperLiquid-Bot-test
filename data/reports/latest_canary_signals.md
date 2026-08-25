# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T05:22:27.164896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `12`; crypto_alt avg `0.0804` n `231`; crypto_major avg `-0.0065` n `8`; equity avg `0.2114` n `122`; fx avg `0.0176` n `6`; index avg `0.0336` n `25`; metal avg `0.0576` n `20`; unknown avg `-0.0854` n `794`
- 1h: commodity avg `-0.0747` n `12`; crypto_alt avg `0.4077` n `231`; crypto_major avg `0.2496` n `8`; equity avg `0.3478` n `122`; fx avg `-0.0162` n `6`; index avg `0.0422` n `25`; metal avg `0.086` n `20`; unknown avg `0.394` n `794`
- 4h: commodity avg `-0.0765` n `12`; crypto_alt avg `1.1003` n `231`; crypto_major avg `0.9193` n `8`; equity avg `1.2517` n `122`; fx avg `0.0102` n `6`; index avg `0.2136` n `25`; metal avg `-0.2931` n `20`; unknown avg `1.0828` n `794`
- 24h: commodity avg `-0.0583` n `12`; crypto_alt avg `1.9342` n `231`; crypto_major avg `2.8665` n `8`; equity avg `0.0046` n `122`; fx avg `0.0364` n `6`; index avg `-0.0419` n `25`; metal avg `-0.07` n `20`; unknown avg `0.6447` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
