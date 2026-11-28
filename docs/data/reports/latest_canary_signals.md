# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T10:52:23.291298+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0074` n `13`; crypto_alt avg `-0.0248` n `239`; crypto_major avg `-0.0009` n `8`; equity avg `-0.0781` n `168`; fx avg `0.0008` n `6`; index avg `-0.0109` n `27`; metal avg `0.0014` n `20`; unknown avg `0.1877` n `1269`
- 1h: commodity avg `0.0073` n `13`; crypto_alt avg `-0.199` n `239`; crypto_major avg `-0.4291` n `8`; equity avg `-0.1469` n `168`; fx avg `0.0027` n `6`; index avg `-0.0112` n `27`; metal avg `-0.0038` n `20`; unknown avg `18.8338` n `1259`
- 4h: commodity avg `-0.0394` n `13`; crypto_alt avg `-0.5371` n `239`; crypto_major avg `-0.9128` n `8`; equity avg `-0.1331` n `168`; fx avg `-0.0029` n `6`; index avg `-0.0141` n `27`; metal avg `0.0086` n `20`; unknown avg `0.0952` n `1213`
- 24h: commodity avg `-0.5594` n `13`; crypto_alt avg `-3.4805` n `239`; crypto_major avg `-3.5616` n `8`; equity avg `-0.7058` n `168`; fx avg `-0.0775` n `6`; index avg `-0.0096` n `27`; metal avg `-0.2824` n `20`; unknown avg `190.6507` n `1087`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
