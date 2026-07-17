# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T09:22:30.873035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0839` n `12`; crypto_alt avg `0.0427` n `230`; crypto_major avg `0.0777` n `8`; equity avg `0.1123` n `96`; fx avg `0.0096` n `6`; index avg `0.0099` n `25`; metal avg `0.072` n `20`; unknown avg `-0.0045` n `768`
- 1h: commodity avg `0.2076` n `12`; crypto_alt avg `0.3295` n `230`; crypto_major avg `0.3037` n `8`; equity avg `0.2981` n `96`; fx avg `0.0176` n `6`; index avg `0.0293` n `25`; metal avg `0.1595` n `20`; unknown avg `-0.0506` n `768`
- 4h: commodity avg `0.1002` n `12`; crypto_alt avg `-0.4828` n `230`; crypto_major avg `-0.3447` n `8`; equity avg `-0.4788` n `96`; fx avg `0.0462` n `6`; index avg `-0.0758` n `25`; metal avg `0.1453` n `20`; unknown avg `-0.0563` n `736`
- 24h: commodity avg `0.1297` n `12`; crypto_alt avg `-1.5189` n `230`; crypto_major avg `-2.7325` n `8`; equity avg `-5.7125` n `94`; fx avg `-0.0255` n `6`; index avg `-0.8203` n `25`; metal avg `-0.7084` n `20`; unknown avg `-0.4988` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
