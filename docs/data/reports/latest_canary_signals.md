# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T08:51:50.422201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0354` n `12`; crypto_alt avg `0.0158` n `230`; crypto_major avg `-0.0095` n `8`; equity avg `-0.1666` n `114`; fx avg `0.0156` n `6`; index avg `-0.0226` n `25`; metal avg `-0.0532` n `20`; unknown avg `-0.0043` n `795`
- 1h: commodity avg `-0.0045` n `12`; crypto_alt avg `0.2099` n `230`; crypto_major avg `0.0642` n `8`; equity avg `-0.6535` n `114`; fx avg `0.0149` n `6`; index avg `-0.0639` n `25`; metal avg `-0.0955` n `20`; unknown avg `-0.0148` n `795`
- 4h: commodity avg `-0.0432` n `12`; crypto_alt avg `0.4733` n `230`; crypto_major avg `0.1803` n `8`; equity avg `-1.0052` n `114`; fx avg `-0.0063` n `6`; index avg `-0.165` n `25`; metal avg `-0.1048` n `20`; unknown avg `0.0125` n `761`
- 24h: commodity avg `0.6097` n `12`; crypto_alt avg `-0.5707` n `230`; crypto_major avg `0.3932` n `8`; equity avg `-2.5255` n `114`; fx avg `0.0181` n `6`; index avg `-0.5102` n `25`; metal avg `-0.2395` n `20`; unknown avg `0.048` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
